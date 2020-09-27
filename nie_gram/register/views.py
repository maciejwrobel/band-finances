from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.
def index(request):
    return render(request, 'register/index.html')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("/start")
    else:
        form = RegisterForm()

    return render(request, 'registration/registration_form.html', {"form":form})