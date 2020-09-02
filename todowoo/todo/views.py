from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import TodoForm
from .models import Todo
from django.utils import timezone


def home(request):
    return render(request, 'todo/index.html')


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
            user = User.objects.create_user(username=username, password=password1)
            user.save()
            login(request, user)
            return redirect('currenttodos')
        except IntegrityError:
            return render(request, 'todo/signupuser.html',
                          {'form': UserCreationForm(),
                           'error': 'This username was already taken!'})


def login_user(request):
    if request.method == 'GET':
        return render(request, 'todo/loginuser.html', {'form': AuthenticationForm()})
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'todo/loginuser.html', {
                'form': AuthenticationForm(),
                'error': 'Incorrect username or password!'
            })

        login(request, user)
        return redirect('currenttodos')


@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


# Todos
@login_required
def current_todos(request):
    todos = Todo.objects.filter(user=request.user, date_completed__isnull=True)
    return render(request, 'todo/current-todos.html', {'todos': todos})


@login_required
def create_todo(request):
    if request.method == 'GET':
        return render(request, 'todo/create-todo.html', {'form': TodoForm()})
    elif request.method == 'POST':
        try:
            form = TodoForm(request.POST)
            new_todo = form.save(commit=False)
            new_todo.user = request.user
            new_todo.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/create-todo.html', {'form': TodoForm()}, {'error': 'Wrong data!'})


@login_required
def view_todo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'todo/view-todo.html', {'todo': todo, 'form': form})
    elif request.method == 'POST':
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todo/view-todo.html', {'todo': todo, 'form': form, 'error': 'Wrong data'})


@login_required
def complete_todo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.date_completed = timezone.now()
        todo.save()
        return redirect('currenttodos')


@login_required
def delete_todo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('currenttodos')


@login_required
def completed_todos(request):
    todos = Todo.objects.filter(user=request.user, date_completed__isnull=False).order_by('-date_completed')
    return render(request, 'todo/completed-todos.html', {'todos': todos})