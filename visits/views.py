import os
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.conf import settings
from main.models import Patient, Visit, Dosage, Disease, Medicine
from django.db.models import Q
from main.templatetags import have_group
from users.forms import DiseaseDataForm, DosageDataForm, MedicineDataForm
from .forms import VisitAddForm

from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from django.http import HttpResponse

from django.views.generic import  CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required(login_url="login")
def visits(request):
    if have_group.is_receptionist(request.user) or have_group.is_doctor(request.user):
        if 'q' in request.GET:
            q = request.GET['q']
            multiple_q = Q(Q(patient__name__icontains=q) | Q(patient__surname__icontains=q))
            data = Visit.objects.filter(multiple_q)
        else:
            data = Visit.objects.all()
        context = {'active_app': 'visits', 'data': data}
        return render(request, 'visits/visits.html', context=context)
    else:
        current_user_id = request.user.id
        patient = Patient.objects.get(user=current_user_id)
        data = Visit.objects.filter(patient=patient.id)
        context = {'active_app': 'visits', 'data': data}
        return render(request, 'visits/visits.html', context=context)

@login_required(login_url="login")
def visit_add(request):

    form=VisitAddForm()
    dosage_form = DosageDataForm()
    disease_form = DiseaseDataForm()
    medicine_form = MedicineDataForm()
    if request.method == 'POST':
        form = VisitAddForm(request.POST)
        dosage_form = DosageDataForm(request.POST)
        disease_form = DiseaseDataForm(request.POST)
        medicine_form = MedicineDataForm(request.POST)
        if form.is_valid() and dosage_form.is_valid() and disease_form.is_valid() and medicine_form.is_valid():
            title = form.cleaned_data['title']
            patient = form.cleaned_data['patient']
            doctor = form.cleaned_data['doctor']
            disease_title = disease_form.cleaned_data['title']
            disease_symptoms = disease_form.cleaned_data['symptoms']
            medicine_description = dosage_form.cleaned_data['description']
            medicine_start_date = dosage_form.cleaned_data['start_date']
            medicine_end_date = dosage_form.cleaned_data['end_date']
            notes = form.cleaned_data['notes']
            date = form.cleaned_data['date']
            medicine_title = medicine_form.cleaned_data['title']
            medicine_property = medicine_form.cleaned_data['property']

            medicine = Medicine.objects.create(title = medicine_title,
                                               property = medicine_property
            )

            dosage = Dosage.objects.create(
                                          medicine=medicine,
                                          description=medicine_description,
                                          start_date=medicine_start_date,
                                          end_date=medicine_end_date,
                                          patient=patient
            )

            disease = Disease.objects.create(title = disease_title,
                                             symptoms = disease_symptoms
            )

            visit = Visit.objects.create(title = title,
                                         patient = patient,
                                         doctor = doctor,
                                         disease = disease,
                                         notes = notes,
                                         date = date,
                                         medicine_dosage = dosage
            )

        return redirect('visits')

    context = {'form': form, 'dosage_form': dosage_form, 'disease_form': disease_form, 'medicine_form': medicine_form,  'active_app': 'visits'}
    return render(request, 'visits/visit_add.html', context=context)

@login_required(login_url="login")
def visit_edit(request, visit_id):
    visit = Visit.objects.get(id=visit_id)
    disease = Disease.objects.get(id=visit.disease_id)
    dosage = Dosage.objects.get(id=visit.medicine_dosage_id)
    visit_form = VisitAddForm(instance=visit)
    disease_form = DiseaseDataForm(instance=disease)
    dosage_form = DosageDataForm(instance=dosage)

    if request.method == "POST":

        visit_form = VisitAddForm(request.POST, instance=visit)
        disease_form = DiseaseDataForm(request.POST, instance=disease)
        dosage_form = DosageDataForm(request.POST, instance=dosage)

        if visit_form.is_valid():
            visit_form.save()
            disease_form.save()
            dosage_form.save()
            return redirect('visits')

    context = {'active_app': 'visits', 'visit': visit, 'visit_form': visit_form, 'disease_form': disease_form,
               'dosage_form': dosage_form}
    return render(request, 'visits/visit_edit.html', context=context)


@login_required(login_url="login")
def view_visit(request, visit_id):

    visit = Visit.objects.get(id=visit_id)
    context = {'active_app': 'visits', 'visit': visit}
    return render(request, 'visits/visit.html', context=context)


@login_required(login_url="login")
def delete_visit(request, visit_id):
    visit = Visit.objects.get(id=visit_id)
    visit.delete()
    return redirect('visits')

@login_required(login_url="login")
def generate_prescription_pdf(request, visit_id):
    # Tworzenie odpowiedzi HTTP z nagłówkiem PDF

    visit = Visit.objects.get(id=visit_id)
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    font_path = os.path.join(settings.BASE_DIR, 'static', 'fonts' , 'static','OpenSans-Medium.ttf')
    logo_path = os.path.join(settings.BASE_DIR, 'static', 'assets', 'brand', 'logo.png')
    if not os.path.exists(font_path):
        raise FileNotFoundError(f"Font not found at {font_path}")
    pdfmetrics.registerFont(TTFont('OpenSansMedium', font_path))
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename= "{visit.patient.name}_{visit.patient.surname}_{timestamp}_recepta.pdf"'

    # Rozmiar strony
    width, height = A4

    # Tworzenie obiektu canvas
    c = canvas.Canvas(response, pagesize=A4)
    c.setFont("OpenSansMedium", 12)
    # Dodanie logo w lewym górnym rogu (zmień ścieżkę do pliku logo)
    try:
        c.drawImage(logo_path, 220, height - 800, width=414, height=261, mask='auto')
    except Exception as e:
        print(f"Error loading logo: {e}")

    # Dodanie nagłówka
    c.setFont("OpenSansMedium", 20)
    c.drawString(260, height - 50, "RECEPTA")
    c.setFont("OpenSansMedium", 9)
    c.drawString(475, height - 20, f"Wrocław, {visit.date}")
    # Dodanie ramki wokół treści recepty
    c.setLineWidth(1)
    c.setStrokeColor(colors.black)
    c.rect(40, height - 300, width - 80, 200, stroke=1, fill=0)
    c.setFont("OpenSansMedium", 12)
    # Treść recepty
    c.drawString(50, height - 120, f"Imię i nazwisko: {visit.patient.name} {visit.patient.surname}")
    c.drawString(360, height - 120, f"Adres: {visit.patient.address.street} {visit.patient.address.number} {visit.patient.address.city}")
    c.drawString(50, height - 200, f"Choroba: {visit.disease.title}")
    c.drawString(50, height - 220, f"Symptomy: {visit.disease.symptoms}")
    c.drawString(50, height - 240, f"Nazwa leku: {visit.medicine_dosage.medicine}")
    c.drawString(50, height - 260, f"Dawkowanie: {visit.medicine_dosage.description}")
    c.drawString(50, height - 280, f"Przyjmować od {visit.medicine_dosage.start_date} do {visit.medicine_dosage.end_date}")

    # Informacje o lekarzu
    c.drawString(380, height - 330, f"Wystawił: {visit.doctor.name} {visit.doctor.surname}")

    # Stopka dokumentu
    c.drawString(40, 30, "Wygenerowano automatycznie przez system")

    # Zakończenie dokumentu
    c.showPage()
    c.save()

    return response