from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from main.models import Patient, Visit, Dosage
from django.db.models import Q
from main.templatetags import have_group


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
    context = {'active_app': 'visits'}
    return render(request, 'visits/visit_edit.html', context=context)