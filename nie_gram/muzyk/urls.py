from django.urls import path, include, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from . import views
from .models import Zespol, Samochod

app_name = 'muzyk'
urlpatterns = [
    path('', views.main, name='main'),
    path('fast/', views.fast, name='fast'),
    path('fast/analiza/', views.analiza, name='analiza'),
    path('fast/wycena/', views.wycena, name='wycena'),
    path('fast/podzial/', views.podzial, name='podzial'),
    path('slow/', views.slow, name='slow'),
    path('lista/', views.ZespolList.as_view(model=Zespol), name="lista"),
    path('update/<int:pk>', views.ZespolUpdate.as_view(model=Zespol), name="update"),
    path('detail/<int:pk>', views.ZespolDetail.as_view(model=Zespol), name="detail"),
    path('create/', views.ZespolCreate.as_view(model=Zespol), name="create"),
    path('delete/<int:pk>', views.ZespolDelete.as_view(model=Zespol), name="delete"),
]