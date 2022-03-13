from django.urls import path, include, reverse_lazy
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('post/view/<slug:slug>/', views.viewpost, name='viewpost'), #should switch this to slug
    path('post/browse/<int:page>/', views.browse, name='browse'),
    path('post/add/', views.addpost, name='addpost'),
    path('post/edit/<slug:slug>/', views.editpost, name='editpost'),
    path('post/delete/<slug:slug>/', views.deletepost, name='deletepost'),
    path('post/postedited/<slug:slug>/', views.postedited, name='postedited'),
    path('post/postadded/<slug:slug>/', views.postadded, name='postadded'),
    path('post/postdeleted/<slug:slug>/', views.postdeleted, name='postdeleted'),
    path('post/toomanyposts/', views.toomanyposts, name='toomanyposts'),
]