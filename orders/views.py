from django.http import HttpResponse
from django.shortcuts import render

from .models import Pizza, Topping, Sub

# Create your views here.
def index(request):

    context = {
        "Pizza": Pizza.objects.all()
    }
    return render(request, "orders/index.html", context)

def menu(request):
    context = {
        "Pizza": Pizza.objects.all()
    }
    return render(request, "orders/menu.html", context)
