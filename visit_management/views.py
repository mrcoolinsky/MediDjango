
from main.models import Visit
from .forms import AppointmentForm
from .models import Visit
from django.shortcuts import render, redirect
def visit_list(request):
    visits = Visit.objects.all()
    return render(request, 'visit_management/visit_list.html', {'visits': visits})




# views.py


# visit_management/views.py
from django.shortcuts import render, redirect
from main.models import Visit
from .forms import AppointmentForm

def make_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # Przetwarzanie formularza, np. zapis wizyty
            # Możesz uzyskać dostęp do pól formularza za pomocą form.cleaned_data
            patient_name = form.cleaned_data['patient_name']
            doctor_name = form.cleaned_data['doctor_name']
            appointment_date = form.cleaned_data['appointment_date']

            # Zapisz wizytę w bazie danych (model Visit z zakładki main)
            Visit.objects.create(
                patient_name=patient_name,
                doctor_name=doctor_name,
                appointment_date=appointment_date
            )

            return redirect('visit_list')  # Przekieruj na stronę listy wizyt w Django Admin
    else:
        form = AppointmentForm()

    context = {'form': form}
    return render(request, 'visit_management/make_appointment.html', context=context)
