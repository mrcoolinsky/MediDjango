from django.db import models
from main.models import Patient
from main.models import Doctor

# models.py
from django.db import models

class Visit(models.Model):
    patient_name = models.CharField(max_length=255)
    doctor_name = models.CharField(max_length=255)
    appointment_date = models.DateTimeField()

    def __str__(self):
        return f"{self.patient_name} - {self.doctor_name} - {self.appointment_date}"


#

