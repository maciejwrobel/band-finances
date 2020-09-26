from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Zespol, Samochod
# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the muzyk index.")

def main(request):
    return render(request, 'muzyk/main.html')

def logowanie(request):
    return render(request, 'register/login.html')

def fast(request):
    return render(request, 'muzyk/fast.html')

def analiza(request):
    return render(request, 'muzyk/analiza.html')

def wycena(request):
    return render(request, 'muzyk/wycena.html')

def podzial(request):
    return render(request, 'muzyk/podzial.html')

def slow(request):
    return render(request, 'muzyk/slow.html')

class ZespolList(ListView):
    model = Zespol


class ZespolDetail(DetailView):
    model = Zespol


class ZespolCreate(CreateView):
    model = Zespol
    fields = '__all__'


class ZespolUpdate(UpdateView):
    model = Zespol
    fields = '__all__'


class ZespolDelete(DeleteView):
    model = Zespol
    success_url = reverse_lazy("muzyk:zespol-lista")


class SamochodList(ListView):
    model = Samochod


class SamochodDetail(DetailView):
    model = Samochod


class SamochodCreate(CreateView):
    model = Samochod
    fields = '__all__'


class SamochodUpdate(UpdateView):
    model = Samochod
    fields = '__all__'


class SamochodDelete(DeleteView):
    model = Samochod
    success_url = reverse_lazy("muzyk:samochod-lista")