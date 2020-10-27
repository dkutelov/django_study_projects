from django.shortcuts import render
import random


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        characters.extend([ch.upper() for ch in characters])

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    if request.GET.get('special-characters'):
        characters.extend(list('!@#$%^&*()_+'))

    new_password = ''
    for x in range(length):
        new_password += random.choice(characters)

    return render(request, 'generator/password.html', {
        'password': new_password
    })


def about(request):
    return render(request, 'generator/about.html')