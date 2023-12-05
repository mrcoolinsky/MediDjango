from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, AdditionalDataForm
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
    form = AdditionalDataForm()

    if request.method == "POST":
        form = AdditionalDataForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            date_of_birth = form.cleaned_data['date_of_birth']
            street = form.cleaned_data['street']
            number = form.cleaned_data['number']
            zip_code = form.cleaned_data['zip_code']
            city = form.cleaned_data['city']

            if patient:
                patient.user = request.user
                patient.name = name
                patient.surname = surname
                patient.date_of_birth = date_of_birth
                patient.address.street = street
                patient.address.number = number
                patient.address.zip_code = zip_code
                patient.address.city = city
                patient.save()
                patient.address.save()
            else:
                address = Address.objects.create(
                    street=street,
                    zip_code=zip_code,
                    number=number,
                    city=city,
                )
                patient = Patient.objects.create(
                    user=request.user,
                    name=name,
                    surname=surname,
                    date_of_birth=date_of_birth,
                    address=address,
            )
            return redirect('dashboard')
        else:
            print("Formularz niepoprawny")
            print(form.errors)

    context = {'patient_data': form}

    return render(request, 'users/patient_data.html', context=context)
