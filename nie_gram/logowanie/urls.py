from django.urls import path

from . import views


# app_name = 'logowanie'
urlpatterns = [
    path('rejestracja', views.rejestracja, name="rejestracja"),
    path('witaj', views.witaj, name="witaj"),
    path('witaj-login', views.witaj_login, name='witaj_login')
]
