from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('post_question/', views.post_question, name='post_question'),
    path('question/<int:pk>/', views.view_question, name='view_question'),
    path('like_answer/<int:pk>/', views.like_answer, name='like_answer'),
]
