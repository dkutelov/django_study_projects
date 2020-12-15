from django.urls import path

from . import views

urlpatterns = [
    path('', views.AppointmentList.as_view(), name='appointment'),
    path('<int:pk>/', views.AppointmentDetail.as_view(), name='appointment detail'),
]