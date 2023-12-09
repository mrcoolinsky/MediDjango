from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, PatientDataForm, AddressDataForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth, Group
from django.contrib.auth import authenticate, login, logout
from main.models import Patient, Address


def login(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
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
            group = Group.objects.get(name='Pacjent')
            user.groups.add(group)
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

    try:
        patient = Patient.objects.get(user=request.user)
    except Patient.DoesNotExist:
        patient = None
    patient_form = PatientDataForm()
    address_form = AddressDataForm()

    if request.method == "POST":
        form = PatientDataForm(request.POST, instance=patient)

        if form.is_valid():
            patient_form.save()
            address_form.save()
            return redirect('dashboard')

    context = {'patient_data': patient_form, 'address_data': address_form}

    return render(request, 'users/patient_data.html', context=context)
