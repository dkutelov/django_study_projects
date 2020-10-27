from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('create/', views.create_expense, name="create_expense"),
    path('edit/<int:pk>/', views.edit_expense, name="edit_expense"),
    path('delete/<int:pk>/', views.delete_expense, name="delete_expense"),
]