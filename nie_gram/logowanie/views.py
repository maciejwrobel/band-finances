from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import reverse
from django.http import HttpResponse

from . import forms


# Create your views here.
def rejestracja(request):
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(reverse("witaj"))
    else:
        form = forms.RegisterForm()
    return render(request, "registration/rejestracja.html", {"form": form})


def witaj(request):
    return HttpResponse("Rejestracja przebiegła pomyślnie")


def witaj_login(request):
    return render(request, "registration/witaj.html")