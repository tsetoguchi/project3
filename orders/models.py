from django.db import models
from django import forms

# Create your models here.

class Pizza(models.Model):
    price = models.DecimalField(max_digits = 6, decimal_places=2)
    size = models.CharField(max_length = 5)
    type = models.CharField(max_length = 64)
    dish = models.CharField(max_length = 64, default='')

    def __str__(self):
        return f"{self.size} {self.type} {self.dish} Pizza - ${self.price}"

class Sub(models.Model):
    price = models.DecimalField(max_digits = 6, decimal_places=2)
    size = models.CharField(max_length = 5)
    type = models.CharField(max_length = 64)

    def __str__(self):
        return f"{self.size} {self.type} Sub - ${self.price}"

class Topping(models.Model):
    name = models.CharField(max_length = 64)
    pizzas = models.ManyToManyField(Pizza, blank = True, related_name = "pizzaToppings")
    subs = models.ManyToManyField(Sub, blank = True, related_name = "subToppings")

    def __str__(self):
        return f"{self.name}"

# Menu options will not be affected when customer creates a new order
class Options(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE, blank = True, null = True)
    topping = models.ForeignKey(Topping, on_delete = models.CASCADE, blank = True, null = True)
    sub = models.ForeignKey(Sub, on_delete = models.CASCADE, blank = True, null = True)

    def returnPizzas(self):
        return f"{self.pizza}"

    def returnSubs(self):
        return f"{self.sub}"

    def returnToppings(self):
        return f"{self.topping}"

    def __str__(self):
        if self.pizza is not None:
            return f"{self.pizza}"
        if self.topping is not None:
            return f"{self.topping}"
        return f"{self.sub}"
# Menu
class Menu(models.Model):
    item = models.ForeignKey(Options, on_delete = models.CASCADE, blank = True)

    def __str__(self):
        return f"{self.item}"

class Cart(models.Model):
    owner = models.CharField(max_length = 5)
    checkedOut = forms.BooleanField(initial=False)
    items = models.CharField(max_length = 64, null = True)