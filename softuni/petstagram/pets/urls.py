from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.list_pets, name='list_pets'),
    path('details/<int:pk>/', views.show_pet_detail, name="pet_details"),
    path('like/<int:pk>/', views.like_pet, name="like_pet"),
    path('edit/<int:pk>/', views.edit_pet, name="edit_pet"),
    path('delete/<int:pk>/', views.delete_pet, name="delete_pet"),
    path('create/', views.create_pet, name="create_pet"),
]