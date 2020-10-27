from django.contrib import admin
from django.urls import path

from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup', views.sign_up_user, name='signupuser'),
    path('login', views.login_user, name='loginuser'),
    path('logout', views.logout_user, name='logoutuser'),
    path('create', views.create_todo, name='createtodo'),
    path('current', views.current_todos, name='currenttodos'),
    path('todo/<int:todo_pk>', views.view_todo, name='viewtodo'),
    path('todo/<int:todo_pk>/complete', views.complete_todo, name='completetodo'),
    path('todo/<int:todo_pk>/delete', views.delete_todo, name='deletetodo'),
    path('completed', views.completed_todos, name='completedtodos'),
]
