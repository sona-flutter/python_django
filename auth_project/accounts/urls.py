from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list_create, name='user-list-create'),
    path('users/<int:pk>/', views.user_detail, name='user-detail'),
]
