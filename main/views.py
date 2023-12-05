from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from main.models import Patient, Address


@login_required(login_url="login")
def dashboard(request):
    permissions = Permission.objects.all()

    context = {'permissions': permissions, 'active_app': 'dashboard'}
    return render(request, 'main/dashboard.html', context=context)


def main(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
        return redirect("login")


@login_required(login_url="login")
def patients(request):
    Patients = Patient.objects.all()

    context = {'patients': Patients, 'active_app': 'patients'}
    return render(request, 'main/patients.html', context=context)
