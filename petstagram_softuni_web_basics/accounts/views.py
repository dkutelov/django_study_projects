from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import SignUpForm
from accounts.models import UserProfile


def user_profile(request, pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'user': user,
        }
        return render(request, 'accounts/user_profile.html', context)


# def signup_user(request):
#     if request.method == 'GET':
#         context = {
#             'form': SignUpForm()
#         }
#         return render(request, 'accounts/signup.html', context)
#     else:
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             profile = UserProfile(
#                 user=user
#             )
#             login(request,user)
#             return redirect('list_pets')
#
#         context = {
#             'form': form
#         }
#         return render(request, 'accounts/signup.html', context)


class SignUpView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('user profile')

    # to login the user
    def form_valid(self, form):
        valid = super().form_valid(form)
        user = form.save()
        profile = UserProfile(user=user)
        profile.save()
        login(self.request, user)
        return valid


def signout_user(request):
    logout(request)
    return redirect('list_pets')

