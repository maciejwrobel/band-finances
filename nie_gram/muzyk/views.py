from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the muzyk index.")


def main(request):
    return render(request, 'muzyk/main.html')


def fast(request):
    return render(request, 'muzyk/fast.html')


def analiza(request):
    return render(request, 'muzyk/analiza.html')


def wycena(request):
    return render(request, 'muzyk/wycena.html')


def podzial(request):
    return render(request, 'muzyk/podzial.html')
