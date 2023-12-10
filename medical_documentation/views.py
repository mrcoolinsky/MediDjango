from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def documentation(request):
    context = {'active_app': 'documentation'}
    return render(request, 'medical_documentation/documentation.html', context=context)