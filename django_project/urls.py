from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .views import news_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', news_index, name='news_index'),
    
]
