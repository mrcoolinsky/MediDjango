from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from main.models import Patient, Address
from users.forms import AdditionalDataForm


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
    all_patients = Patient.objects.all()

    context = {'all_patients': all_patients, 'active_app': 'patients'}
    return render(request, 'main/patients.html', context=context)


@login_required(login_url="login")
def edit_patient(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)
    return render(request, 'main/edit_patient.html', {'patient_id': patient_id, 'patient': patient})
