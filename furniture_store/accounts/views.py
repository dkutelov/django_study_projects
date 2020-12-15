from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView

from accounts.models import ProfileUser


def redirect_user(request):
    url = f'/furniture/'
    return HttpResponseRedirect(url)


class UserDetail(DetailView):
    model = ProfileUser
    template_name = 'user_profile.html'
    context_object_name = 'user'


class SignUp(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/furniture/'
    template_name = 'signup.html'

