from django.urls import path
from . import views
from django.urls import include

urlpatterns = [

    path('', views.main, name="main"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('patients', views.patients, name="patients"),
    path('patients/edit/<int:patient_id>/', views.edit_patient, name="edit_patient"),
    path('doctors', views.doctors, name="doctors"),
    path('doctors/edit/<int:doctor_id>/', views.edit_doctor, name="edit_doctor"),
    path('visit-management/', include('visit_management.urls')),

]