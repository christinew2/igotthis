from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('todos/', views.todos_index, name='todos_index'),
    path('todos/create/', views.TodoCreate.as_view(), name='todos_create'),
    path('todos/<int:pk>/update/', views.TodoUpdate.as_view(), name='todos_update'),
    path('todos/<int:pk>/delete/', views.TodoDelete.as_view(), name='todos_delete'),
    path('todos/<int:todo_id>/cross_off/', views.cross_off, name="cross_off"),
    path('todos/<int:todo_id>/uncross_off/', views.uncross_off, name="uncross_off"),
    path('accounts/signup/', views.signup, name='signup')
]