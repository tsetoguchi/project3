from django.contrib import admin
from .models import Pizza, Topping, Sub, Menu, Cart, Options

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Sub)
admin.site.register(Menu)
admin.site.register(Cart)
admin.site.register(Options)