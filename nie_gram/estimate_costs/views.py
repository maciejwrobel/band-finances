from django.shortcuts import render



# Create your views here.
def main_page(request):
    return render(request, 'estimate_costs/main_page.html')

def add_bands_profile(request):
    if request.method == "POST":
        print(request.POST)

    return render(request, 'estimate_costs/add_bands_profile.html')

def order_valuation(request):
    if request.method == "POST":
        print(request.POST)

    return render(request, 'estimate_costs/order_valuation.html')
