from django.contrib import admin
from django.urls import path

from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup', views.sign_up_user, name='signupuser'),
    path('current', views.current_todos, name='currenttodos'),
]
