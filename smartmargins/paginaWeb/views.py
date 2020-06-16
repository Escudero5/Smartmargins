from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request,"paginaWeb/home.html")


def plansAndPrices(request):
    return render(request,"paginaWeb/plansandprices.html")

def accountDetails(request):
    return render(request,"paginaWeb/accountdetails.html")

def payment(request):
    return render(request,"paginaWeb/payment.html")

def dashboard(request):
    return render(request,"paginaWeb/dashboard.html")

def products(request):
    return render(request,"paginaWeb/products.html")

def salesChannels(request):
    return render(request,"paginaWeb/saleschannels.html")

def competitors(request):
    return render(request,"paginaWeb/competitors.html")

def strategySettings(request):
    return render(request,"paginaWeb/strategysettings.html")
