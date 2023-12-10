from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.base, name='base'),
    path('users/', views.users, name='users'),
    path('blogs/', views.blogs, name='blogs'),
    path('comments/', views.comments, name='comments'),
    path('categories/', views.categories, name='categories'),
    path('blogdetails', views.blogdetails, name='blogdetails'),
]
