from django.contrib import admin
# from django.contrib.auth.models import User
# from django.shortcuts import render
from django.urls import path, include

# from django101.views import index, UsersListView, GamesListView

urlpatterns = [
    path('', include('django102.urls')),
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', index),
#     path('2/', UsersListView.as_view()),
#     path('games/', GamesListView.as_view())
# ]
