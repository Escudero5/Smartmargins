from django.urls import path
from paginaWeb import views


urlpatterns = [
    path('',views.home, name="home"),
    path('plansandprices',views.plansAndPrices, name="plansandprices"),
    path('accountdetails',views.accountDetails, name="accountdetails"),
    path('payment',views.payment, name="payment"),
    path('dashboard',views.dashboard, name="dashboard"),
    path('products',views.products, name="products"),
    path('saleschannels',views.salesChannels, name="saleschannels"),
    path('competitors',views.competitors, name="competitors"),
    path('strategysettings',views.strategySettings, name="strategysettings"),
]