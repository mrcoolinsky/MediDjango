from django.shortcuts import render, redirect
from .forms import CreateUserForm


# Create your views here.


def login(request):
    return render(request, 'users/login.html')


def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect("login")

    context = {'reformist': form}
    return render(request, 'users/register.html', context=context)
