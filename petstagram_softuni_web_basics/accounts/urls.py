from django.contrib.auth.views import LoginView
from django.urls import path, include
from . import views

urlpatterns = [
    # path('signin/', LoginView.as_view(template_name='registration/signin.html'), name='signin user'),
    path('', include('django.contrib.auth.urls')),
    path('profile/', views.user_profile, name="user profile"),
    path('profile/<int:pk>/', views.user_profile, name="user profile"),
    # path('signup/', views.signup_user, name="signup user"),
    path('signup/', views.SignUpView.as_view(), name="signup user"),
    path('signout/', views.signout_user, name="signout user"),
]
