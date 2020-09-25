from django.urls import path, include
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from . import views
from . import models

app_name = 'muzyk'
urlpatterns = [
    path('', views.main, name='main'),
    path('fast/', views.fast, name='fast'),
    path('fast/analiza/', views.analiza, name='analiza'),
    path('fast/wycena/', views.wycena, name='wycena'),
    path('fast/podzial/', views.podzial, name='podzial'),
    path('slow/', views.slow, name='slow'),
]