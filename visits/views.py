from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from main.models import Patient, Visit, Dosage, Disease
from django.db.models import Q
from main.templatetags import have_group
from users.forms import VisitDataForm, DiseaseDataForm, DosageDataForm


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
        return redirect('view_visit', request.user.id)


@login_required(login_url="login")
def visit_edit(request, visit_id):
    visit = Visit.objects.get(id=visit_id)
    disease = Disease.objects.get(id=visit.disease_id)
    dosage = Dosage.objects.get(id=visit.medicine_dosage_id)
    visit_form = VisitDataForm(instance=visit)
    disease_form = DiseaseDataForm(instance=disease)
    dosage_form = DosageDataForm(instance=dosage)

    if request.method == "POST":

        visit_form = VisitDataForm(request.POST, instance=visit)
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