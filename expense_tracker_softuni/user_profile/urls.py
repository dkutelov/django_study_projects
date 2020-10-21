from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name="profile"),
    path('edit/', views.edit_profile, name="edit_profile"),
    path('delete/', views.delete_profile, name="delete_profile"),
]
