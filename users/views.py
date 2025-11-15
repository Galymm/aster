from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

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
