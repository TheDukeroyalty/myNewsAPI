from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # URL pattern for the main page
    path('dogs/', views.dogs, name='dogs'),  # URL pattern for the dogs page
]
