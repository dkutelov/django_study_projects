from django.urls import path, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('2/', views.IndexTemplateView.as_view(), name="index 2"),
    path('3/', TemplateView.as_view(template_name='cbv/index.html'), name="index 3"),
    path('list/', views.PetsListView.as_view(), name='pets list'),
    path('details/<int:pk>', views.PetDetailsView.as_view(), name="pet details"),
    path('create/', views.PetCreateView.as_view(), name="cbv pet create"),
]
