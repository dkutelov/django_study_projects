from django.urls import path

from books import views

urlpatterns = [
    path('', views.index, name="book index"),
    path('create/', views.create, name="book create"),
    path('edit/<int:pk>/', views.edit, name="book edit"),
]
