from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('home', views.index, name="index"),
    path('login', views.LoginUserView.as_view(), name="login"),
    path('registration', views.RegisterUserView.as_view(), name="reg"),
    path('add_todo/', views.add_todo, name="add"),
    path('delete_all', views.delete_all, name='delete_all'),
    path('check/<todo_id>', views.check_todo, name="check"),
    path('uncheck/<todo_id>', views.uncheck_todo, name="uncheck"),
    path('delete_checked', views.delete_completed, name='delete_checked'),
    path('view', views.TodoList, name="view"),
    path('details/<int:pk>/',views.TodoDetail.as_view(),name="details"),



]
