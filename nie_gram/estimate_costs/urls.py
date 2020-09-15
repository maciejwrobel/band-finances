from django.urls import path, include

from . import views

app_name ="estimate_costs"

urlpatterns = [
    path('', views.main_page, name="main_page"),
    path('add_bands_profile', views.add_bands_profile, name="add_bands_profile"),
    path('order_valuation', views.order_valuation, name="order_valuation"),
]