from django.contrib import admin
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name = 'list'),
    path('article/<slug:slug>', views.article_details, name = 'detail'),
    path('create/', views.article_create, name = 'create'),
]
