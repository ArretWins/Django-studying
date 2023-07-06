from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('add_todo', views.add_todo, name='add_todo'),
    path('update/<int:todo_id>/', views.update, name='update'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
]
