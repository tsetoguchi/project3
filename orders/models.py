from django.db import models
from django import forms

# Create your models here.

class Pizza(models.Model):
    price = models.DecimalField(max_digits = 6, decimal_places=2)
    size = models.CharField(max_length = 5)
    type = models.CharField(max_length = 64)

    def __str__(self):
        return f"{self.size} {self.type} Pizza - ${self.price}"

class Topping(models.Model):
    name = models.CharField(max_length = 64)
    pizzas = models.ManyToManyField(Pizza, blank = True, related_name = "toppings")

class Sub(models.Model):
    price = models.DecimalField(max_digits = 6, decimal_places=2)
    size = models.CharField(max_length = 5)
    type = models.CharField(max_length = 64)

    def __str__(self):
        return f"{self.size} {self.type} Sub - ${self.price}"

class Options(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE, blank = True, null = True)
    topping = models.ForeignKey(Topping, on_delete = models.CASCADE, blank = True, null = True)
    sub = models.ForeignKey(Sub, on_delete = models.CASCADE, blank = True, null = True)

    def __str__(self):
        return f"{self.pizza}"

class Menu(models.Model):
    item = models.ForeignKey(Options, on_delete = models.CASCADE, blank = True)

class Cart(models.Model):
    owner = models.CharField(max_length = 5)