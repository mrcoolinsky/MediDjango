from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, AdditionalDataForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


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
            user = form.save()

            auth.login(request, user)
            return redirect("patient_data")
        else:
            print("Formularz niepoprawny")
            print(form.errors)

    context = {'register': form}
    return render(request, 'users/register.html', context=context)


def user_logout(request):
    auth.logout(request)

    return redirect("login")


@login_required(login_url="login")
def patient_data(request):
    return render(request, 'users/patient_data.html')
