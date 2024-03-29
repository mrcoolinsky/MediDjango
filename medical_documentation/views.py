from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from main.models import Patient, Visit, Dosage
from django.db.models import Q
from main.templatetags import have_group


@login_required(login_url="login")
def documentation(request):
    if have_group.is_receptionist(request.user) or have_group.is_doctor(request.user):
        data = None
        if 'q' in request.GET:
            q = request.GET['q']
            multiple_q = Q(Q(name__icontains=q) | Q(surname__icontains=q))
            data = Patient.objects.filter(multiple_q)
        context = {'active_app': 'documentation', 'data': data}
        return render(request, 'medical_documentation/documentation.html', context=context)
    else:
        return redirect('view_documentation', request.user.id)


@login_required(login_url="login")
def view_documentation(request, patient_id):
    if have_group.is_receptionist(request.user):

        patient = Patient.objects.get(id=patient_id)
        doc_data = Visit.objects.filter(patient=patient.id)
        medi_data = Dosage.objects.filter(patient=patient.id)

        for data in doc_data:
            print(have_group.is_receptionist)
            print(have_group.is_doctor)
            print(data.patient.name)

        for data in medi_data:
            print(data.start_date)

        context = {'active_app': 'documentation', 'documentation': doc_data, 'patient': patient, 'medicine': medi_data}

        return render(request, 'medical_documentation/view_documentation.html', context=context)
    else:
        current_user_id = request.user.id
        patient = Patient.objects.get(user=current_user_id)
        doc_data = Visit.objects.filter(patient=patient.id)
        medi_data = Dosage.objects.filter(patient=patient.id)
        context = {'active_app': 'documentation', 'documentation': doc_data, 'patient': patient, 'medicine': medi_data}
        return render(request, 'medical_documentation/view_documentation.html', context=context)
