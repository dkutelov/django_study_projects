from django.shortcuts import render, redirect

from expense.forms import ExpenseForm, DeleteExpenseForm
from expense.models import Expense
from user_profile.models import Profile
from user_profile.forms import ProfileForm


def get_current_profile():
    return Profile.objects.first()


def home_page(request):
    if request.method == 'GET':
        profile = Profile.objects.all()

        if not profile:
            context = {
                'form': ProfileForm(label_suffix='')
            }
            return render(request, 'homepage/home-no-profile.html', context)

        else:
            expenses = Expense.objects.all()
            profile = profile[0]
            profile.balance = profile.budget - sum([expense.price for expense in expenses])
            context = {
                'expenses': expenses,
                'profile': profile,
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
        profile = form.save(commit=False)
        profile.full_clean()  # check what full_clean
        profile.save()
        return render(request, 'homepage/home-with-profile.html')


def persist_expense(request, expense, html_template):
    if request.method == 'GET':
        return render(request, f'expense/{html_template}.html', {
            'form': ExpenseForm(instance=expense),
            'expense_id': expense.id
        })

    elif request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)

        if not form.is_valid():
            return render(request, f'expense/{html_template}.html', {'form': form})

        expense = form.save(commit=False)
        expense.profile = get_current_profile()
        expense.save()
        return redirect('home_page')


def create_expense(request):
    return persist_expense(request, Expense(), 'expense-create')


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    return persist_expense(request, expense, 'expense-edit')


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)

    if request.method == 'GET':
        return render(request, 'expense/expense-delete.html', {
            'form': DeleteExpenseForm(label_suffix='', instance=expense)
        })

    elif request.method == 'POST':
        expense.delete()
        return redirect('home_page')






