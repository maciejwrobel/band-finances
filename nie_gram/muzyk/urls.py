from django.contrib.auth.decorators import login_required
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
    path('slow/', login_required(views.slow), name='slow'),
    path('zespol-lista/', login_required(views.ZespolList.as_view(model=Zespol)), name="zespol-lista"),
    path('zespol-update/<int:pk>', login_required(views.ZespolUpdate.as_view(model=Zespol)), name="zespol-update"),
    path('zespol-detail/<int:pk>', login_required(views.ZespolDetail.as_view(model=Zespol)), name="zespol-detail"),
    path('zespol-create/', login_required(views.ZespolCreate.as_view(model=Zespol)), name="zespol-create"),
    path('zespol-delete/<int:pk>', login_required(views.ZespolDelete.as_view(model=Zespol)), name="zespol-delete"),
    path('samochod-lista/', login_required(views.SamochodList.as_view(model=Samochod)), name="samochod-lista"),
    path('samochod-update/<int:pk>', login_required(views.SamochodUpdate.as_view(model=Samochod)), name="samochod-update"),
    path('samochod-detail/<int:pk>', login_required(views.SamochodDetail.as_view(model=Samochod)), name="samochod-detail"),
    path('samochod-create/', login_required(views.SamochodCreate.as_view(model=Samochod)), name="samochod-create"),
    path('samochod-delete/<int:pk>', login_required(views.SamochodDelete.as_view(model=Samochod)), name="samochod-delete"),
]