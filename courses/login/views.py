from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import User


def signup(request: HttpRequest):
    return render(request, "signup.html")


def register_user(request: HttpRequest):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        role = request.POST.get("role")

        if not username or not password or not email:
            return render(
                request, "register.html", {"error": "Todos os campos são obrigatórios."}
            )

        user = User.objects.create_user(username, email, password, role=role)
        user.save()
        return redirect("/")


def login_view(request: HttpRequest):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if user.role == "teacher":
                return redirect("/home")
            return redirect("/student_home")
        else:
            return render(request, "login.html", {"error": "Credenciais inválidas"})
    return render(request, "login.html")


def home(request: HttpRequest):
    return render(request, "home.html", {"user": request.user})
