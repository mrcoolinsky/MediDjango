from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from main.models import Patient, Address, Doctor
from users.forms import PatientDataForm, AddressDataForm


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
    patient = Patient.objects.get(id=patient_id)
    address_id = patient.address.id
    address = Address.objects.get(id=address_id)
    patient_form = PatientDataForm(instance=patient)
    address_form = AddressDataForm(instance=address)

    if request.method == "POST":

        patient_form = PatientDataForm(request.POST, instance=patient)
        address_form = AddressDataForm(request.POST, instance=address)

        if patient_form.is_valid() and address_form.is_valid():
            address_form.save()
            patient_form.save()
            return redirect('patients')

    context = {'patient_id': patient_id, 'patient': patient, 'patient_form': patient_form, 'address_form': address_form}
    return render(request, 'main/edit_patient.html', context=context)


@login_required(login_url="login")
def doctors(request):
    all_doctors = Doctor.objects.all()

    context = {'all_doctors': all_doctors, 'active_app': 'doctors'}
    return render(request, 'main/doctors.html', context=context)
