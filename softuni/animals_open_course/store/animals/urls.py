from django.urls import path, re_path
from . import views

app_name = 'animals'

urlpatterns = [
    re_path('^all/$', views.all_animals, name="allanimals"),
    path('api/all/', views.all_animals_json, name="allanimalsjson"),
    path('all-dogs/', views.all_dogs, name="alldogs"),
    path('all-cats/', views.all_cats, name="allcats"),
    path('<int:animal_id>/', views.animal_by_id, name="animalbyid"),
    path('api/<int:animal_id>/', views.animal_by_id_json, name="animalbyidjson"),

    path('class-all/', views.AnimalList.as_view(), name='list'),
    path('create/', views.AnimalCreate.as_view(), name="create"),
    path('update/<int:pk>/', views.AnimalUpdate.as_view(), name="update"),
    path('delete/<int:pk>/', views.AnimalDelete.as_view(), name="delete"),
    path('details/<int:pk>/', views.AnimalDetail.as_view(), name="detail"),
]