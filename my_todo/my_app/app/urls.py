from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_todo, name='add_todo'),
    path('update/<int:todo_id>/', views.update, name='update'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
    path('full_note/<int:todo_id>/', views.full_note, name='full_note'),
    path('edit/<int:todo_id>/', views.edit, name='edit'),
]
