from django.http import HttpResponse
from django.shortcuts import render


def index(req):
    return HttpResponse('Hello, you are at the pool index page')
