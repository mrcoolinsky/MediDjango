from django.urls import path
from . import views

urlpatterns = [

    path('', views.main, name="main"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('patients', views.patients, name="patients"),
    path('patients/edit/<int:patient_id>/', views.edit_patient, name="edit_patient"),
    path('doctors', views.doctors, name="doctors"),

]