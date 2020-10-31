from django.shortcuts import render, redirect

from expense.models import Expense
from user_profile.forms import ProfileForm
from user_profile.models import Profile


def get_profile_balance(current_profile):
    expenses = Expense.objects.filter(profile=current_profile)
    return current_profile.budget - sum([expense.price for expense in expenses])


def profile(request):
    current_profile = Profile.objects.all()[0]
    current_profile.balance = get_profile_balance(current_profile)
    context = {
        'profile': current_profile,
    }
    return render(request, 'profile/profile.html', context)


def edit_profile(request):
    current_profile = Profile.objects.all()[0]
    context = {
        'form': ProfileForm(instance=current_profile, label_suffix='')
    }

    if request.method == 'GET':
        return render(request, 'profile/profile-edit.html', context)

    elif request.method == 'POST':
        form = ProfileForm(request.POST, instance=current_profile)

        if not form.is_valid():
            return render(request, 'profile/profile-edit.html', {'form': form})

        form.save()
        return redirect('profile')


def delete_profile(request):
    if request.method == 'GET':
        return render(request, 'profile/profile-delete.html')

    elif request.method == 'POST':
        current_profile = Profile.objects.all()[0]
        current_profile.delete()
        return redirect('home_page')
