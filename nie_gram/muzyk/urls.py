from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main),
    path('fast/', views.fast),
    path('logowanie/', views.logowanie),
    path('fast/analiza/', views.analiza),
    path('fast/wycena/', views.wycena),
    path('fast/podzial/', views.podzial),
]