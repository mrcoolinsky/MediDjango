from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

from main.models import Patient

from django.contrib.auth.decorators import login_required


def login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
    context = {'loginform': form}
    return render(request, 'users/login.html', context=context)


def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("login")

        else:
            print("Formularz niepoprawny")
            print(form.errors)

    context = {'register': form}
    return render(request, 'users/register.html', context=context)


def user_logout(request):
    auth.logout(request)

    return redirect("main")


def widok(request):
    obj = Patient.objects.get(id=2)

    context = {'imie': obj.Name,
               'nazwisko': obj.Surname

               }
    return render(request, 'users/test.html', context=context)
