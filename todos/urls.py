from django.urls import path
from . import views


app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    # todos/
    path('create_todo/', views.create_todo, name='create_todo'),
    #todos/create_todo/
    path('<int:todo_pk>/', views.detail, name='detail'),
    #todos/.../
]