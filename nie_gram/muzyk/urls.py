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
    path('zespol-lista/', views.ZespolList.as_view(model=Zespol), name="zespol-lista"),
    path('zespol-update/<int:pk>', views.ZespolUpdate.as_view(model=Zespol), name="zespol-update"),
    path('zespol-detail/<int:pk>', views.ZespolDetail.as_view(model=Zespol), name="zespol-detail"),
    path('zespol-create/', views.ZespolCreate.as_view(model=Zespol), name="zespol-create"),
    path('zespol-delete/<int:pk>', views.ZespolDelete.as_view(model=Zespol), name="zespol-delete"),
    path('samochod-lista/', views.SamochodList.as_view(model=Samochod), name="samochod-lista"),
    path('samochod-update/<int:pk>', views.SamochodUpdate.as_view(model=Samochod), name="samochod-update"),
    path('samochod-detail/<int:pk>', views.SamochodDetail.as_view(model=Samochod), name="samochod-detail"),
    path('samochod-create/', views.SamochodCreate.as_view(model=Samochod), name="samochod-create"),
    path('samochod-delete/<int:pk>', views.SamochodDelete.as_view(model=Samochod), name="samochod-delete"),
]