from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from partner.models import addshop  # Importing the addshop model from the partner app

def homepage(request):
    return render(request, "home.html")

def shoplist(request):
    shops = addshop.objects.all()
    if request.GET.get('search'):
         shops = shops.filter(shop_name__icontains = request.GET.get('search'))
        
    return render(request, "shop.html", {'shops': shops})


def becomepart(request):
    return render(request, "/")

def signup(request):
    return render(request, "signup.html")
