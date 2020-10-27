from django.shortcuts import render, redirect

from expense.forms import ExpenseForm
from expense.models import Expense
from user_profile.models import Profile
from user_profile.forms import ProfileForm


def get_current_profile():
    profile = Profile.objects.all()
    if profile:
        return profile[0]


def home_page(request):
    if request.method == 'GET':
        profile = Profile.objects.all()

        if not profile:
            context = {
                'form': ProfileForm(label_suffix='')
            }
            return render(request, 'homepage/home-no-profile.html', context)
        else:
            profile = profile[0]
            expenses = Expense.objects.all()
            balance = profile.budget - sum([expense.price for expense in expenses])
            context = {
                'expenses': expenses,
                'profile': profile,
                'balance': balance
            }
            return render(request, 'homepage/home-with-profile.html', context)

    elif request.method == 'POST':
        form = ProfileForm(request.POST)
        if not form.is_valid():
            context = {
                'form': ProfileForm(),
                'errors': form.errors
            }
            return render(request, 'homepage/home-no-profile.html', context)
        form.save()
        return render(request, 'homepage/home-with-profile.html')


def persist_expense(request, expense, html_template, pk=None, on_delete=False):
    if request.method == 'GET':
        context = {
            'form': ExpenseForm(label_suffix='', instance=expense)
        }
        if pk:
            context['expense_id'] = pk

        if on_delete:
            for key in context['form'].fields.keys():
                context['form'].fields[key].widget.attrs['disabled'] = True

        return render(request, f'expense/{html_template}.html', context)

    elif request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)

        if not on_delete and not form.is_valid():
            context = {
                'form': ExpenseForm(label_suffix='', instance=expense),
                'errors': form.errors
            }
            return render(request, f'expense/{html_template}.html', context)

        if not on_delete:
            profile = get_current_profile()
            expense.profile = profile
            expense.save()
        else:
            expense.delete()

        return redirect('home_page')


def create_expense(request):
    return persist_expense(request, Expense(), 'expense-create')


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    return persist_expense(request, expense, 'expense-edit', pk)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    return persist_expense(request, expense, 'expense-delete', pk, on_delete=True)






