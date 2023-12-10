from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from main.models import Patient
from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test
from main.templatetags import have_group


@login_required(login_url="login")
@user_passes_test(have_group.is_receptionist)
def documentation(request):
    data = None
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(name__icontains=q) | Q(surname__icontains=q))
        data = Patient.objects.filter(multiple_q)
    context = {'active_app': 'documentation', 'data': data}
    return render(request, 'medical_documentation/documentation.html', context=context)
