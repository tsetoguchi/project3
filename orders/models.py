from django.db import models

# Create your models here.

class Pizza(models.Model):
    price = models.DecimalField(max_digits = 6, decimal_places=2)
    size = models.CharField(max_length = 5)
    type = models.CharField(max_length = 64)

    def __str__(self):
        return f"A {self.size} {self.type} pizza is ${self.price}"

class Topping(models.Model):
    name = models.CharField(max_length = 64)
    pizzas = models.ManyToManyField(Pizza, blank = True, related_name = "toppings")

class Sub(models.Model):
    price = models.DecimalField(max_digits = 6, decimal_places=2)
    size = models.CharField(max_length = 5)
    type = models.CharField(max_length = 64)

    def __str__(self):
        return f"A {self.size} {self.type} sub is ${self.price}"

class Menu(models.Model):
    pizzas = models.ForeignKey(Pizza, on_delete = models.CASCADE, related_name="pizzas")
    subs = models.ForeignKey(Sub, on_delete = models.CASCADE, related_name="subs")
    toppings = models.ForeignKey(Topping, on_delete = models.CASCADE, related_name="toppings")