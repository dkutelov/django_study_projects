from django.urls import path, include

from . import views

urlpatterns = [
    path('auth/', include('rest_auth.urls')),
    path('doctors/', views.DoctorList.as_view(), name='doctors list'),
    path('contact/', views.ContactForm.as_view(), name='contact form'),
]