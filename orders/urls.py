from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("menu", views.menu, name="menu"),
    path("register", views.register, name="register"),
    path("successfulRegister", views.successfulRegister, name="successfulRegister"),
    path("unsuccessfulRegister", views.unsuccessfulRegister, name="unsuccessfulRegister"),
    path("loginPage", views.loginPage, name="loginPage"),
    path("successfulLogin", views.successfulLogin, name="successfulLogin"),
    path("unsuccessfulLogin", views.unsuccessfulLogin, name="unsuccessfulLogin")
]
