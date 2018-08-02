from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import auth

from .models import Pizza, Topping, Sub, Menu, Cart, Options

# Create your views here.
def index(request):

    context = {
        "Pizza": Pizza.objects.all()
    }
    return render(request, "orders/index.html", context)

def register(request):

    return render(request, "orders/register.html")

def successfulRegister(request):

    # Register user into database
    if request.method == "POST":
        username = (request.POST["username"])
        # email = (request.POST["email"])
        password = (request.POST["password"])
        user = User.objects.get(username=username)
        print(user)
        print('*******************')
        if user.DoesNotExist:
            user = User.objects.create_user(username = username, password = password)
            return render(request, "orders/successfulRegister.html")
        return render(request, "orders/unsuccessfulRegister.html")

def unsuccessfulRegister(request):

    return render(request, "orders/unsuccessfulRegister.html")

def loginPage(request):

    return render(request, "orders/loginPage.html")

def successfulLogin(request):
    # Register user into database
    if request.method == "POST":
        email = (request.POST["email"])
        password = (request.POST["password"])
        user = authenticate(password = password, email = email)
        # exists = User.objects.get(email = '{email}')
        # if exists is None:
        #     return render(request, "orders/unsuccessfulLogin.html")
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, "orders/successfulLogin.html")
        else:
            return render(request, "orders/unsuccessfulLogin.html")


def unsuccessfulLogin(request):

    return render(request, "orders/unsuccessfulLogin.html")

def menu(request):
    context = {
        "Pizza": Pizza.objects.all(),
        "Menu": Pizza.toppings.all()
    }
    return render(request, "orders/menu.html", context)

