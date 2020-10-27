from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET
from django.views.generic import ListView

from django102.models import Game


def index(request):
    title = 'Softuni Django 101'
    users = User.objects.all()
    context = {
        'title': title,
        'users': users,
    }
    return render(request, 'index.html', context)


# just to visualize data
class UsersListView(ListView):
    model = User
    template_name = 'index2.html'
    queryset = User.objects.all().order_by('-username')

    def get_context_object_name(self, object_list):
        return 'users'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = 'From class view'
        return context


class GamesListView(ListView):
    model = Game
    template_name = 'games.html'

    def get_context_object_name(self, object_list):
        return 'games'


def something(request):
    return HttpResponse("It works!")


@require_GET
def method_demo(request):
    context = {
        'name': 'dari'
    }

    if request.content_type == 'application/json':
        return JsonResponse(context)

    return render(request, 'method-demo.html', context)