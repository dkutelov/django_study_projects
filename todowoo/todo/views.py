from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login


def sign_up_user(request):
    if request.method == 'GET':
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})
    elif request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return render(request, 'todo/signupuser.html',
                          {'form': UserCreationForm(),
                           'error': 'Passwords did not match!'})

        try:
            user = User.objects.create_user(username, password1)
            user.save()
            login(request, user)
            return redirect('currenttodos')
        except IntegrityError:
            return render(request, 'todo/signupuser.html',
                          {'form': UserCreationForm(),
                           'error': 'This username was already taken!'})


def current_todos(request):
    return render(request, 'todo/current-todos.html')