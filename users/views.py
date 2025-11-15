from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def create_admin(request):
    username = 'admin'
    email = 'admin@example.com'
    password = 'StrongPassword123'  # поставь свой пароль

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        return HttpResponse("Суперпользователь создан!")
    else:
        return HttpResponse("Пользователь уже существует.")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = User.objects.create_user(username=username, password=password)

        # по умолчанию — Reader
        reader_group = Group.objects.get(name="Reader")
        user.groups.add(reader_group)

        return redirect('login')

    return render(request, "users/register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, "users/login.html", {"error": "Неверные данные"})

    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def profile(request):
    return render(request, "users/profile.html")
