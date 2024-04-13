from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect

def homepage(request):
    return render(request, "home.html")

def shoplist(request):
    return render(request, "shop.html")

def becomepart(request):
    return render(request, "becomepart.html")

def signup(request):
    return render(request, "signup.html")

def addshop(request):
    return render(request, "addshop.html")