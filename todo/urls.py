from django.urls import path, include
from django.conf.urls import url

from .views import RegistrationSuccess
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('login', views.LoginUserView.as_view(), name="login"),
    path('registration', views.RegisterUserView.as_view(), name="reg"),
    path('registration/<str:key>', RegistrationSuccess.as_view(), name='success'),
    path('add_todo/', views.TodoAddView.as_view(), name="add"),
    # path('delete_all', views.delete_all, name='delete_all'),
    # path('check/<todo_id>', views.check_todo, name="check"),
    # path('uncheck/<todo_id>', views.uncheck_todo, name="uncheck"),
    # path('delete_checked', views.delete_completed, name='delete_checked'),
    path('list', views.TodoListView.as_view(), name="list"),
    path('delete/<int:pk>/', views.TodoDeleteView.as_view(), name="delete"),
    path('details/<int:pk>/', views.TodoDetailView.as_view(), name="details"),
    path('update/<int:pk>/', views.TodoUpdateView.as_view(), name="update"),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('userlist', views.AduserListView.as_view(), name="userlist"),

]
