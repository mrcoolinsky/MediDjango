from django.db import models
from django.contrib.auth.models import User, Group


class Address(models.Model):
    street = models.CharField(max_length=20)
    number = models.CharField(max_length=4)
    zip_code = models.CharField(max_length=6)
    city = models.CharField(max_length=20)

    def __str__(self):
        return str(self.street + " " + self.number + ", " + self.city)


class Doctor(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    address = models.OneToOneField(Address, null=False, on_delete=models.CASCADE, default="")
    name = models.CharField(max_length=20, null=False, default="")
    surname = models.CharField(max_length=20, null=False, default="")
    phone_number = models.CharField(default="", null=False, max_length=9)
    specialization = models.CharField(max_length=50, null=False, default="")

    def __str__(self):
        return f"{self.name} {self.surname}"


class Medicine(models.Model):
    title = models.CharField(null=False, default="", max_length=20)
    property = models.CharField(null=True, max_length=50)

    def __str__(self):
        return str(self.title)


class Dosage(models.Model):
    start_date = models.DateField(null=False, default='2000-01-01')
    end_date = models.DateField(null=False, default='2000-01-01')
    medicine = models.ForeignKey(Medicine, on_delete=models.SET_NULL, null=True)
    patient = models.ForeignKey("Patient", on_delete=models.SET_NULL, null=True)
    description = models.CharField(null=False, default="", max_length=25)

    def __str__(self):
        return f"{self.medicine}, {self.patient.name} {self.patient.surname}"


class Disease(models.Model):
    title = models.CharField(null=False, default="", max_length=20)
    symptoms = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self):
        return str(self.title)


class Patient(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default="")
    surname = models.CharField(max_length=30, default="")
    address = models.OneToOneField(Address, null=True, on_delete=models.CASCADE)
    date_of_birth = models.DateField(default='2000-01-01')
    phone_number = models.CharField(default="", null=False, max_length=9)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Visit(models.Model):
    title = models.CharField(null=False, default="", max_length=20)
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(Doctor,on_delete=models.SET_NULL, null=True)
    disease = models.ForeignKey(Disease,on_delete=models.SET_NULL, null=True)
    medicine_dosage = models.OneToOneField(Dosage, on_delete=models.CASCADE, null=True,blank=True)
    notes = models.CharField(null=True, blank=True, max_length=300)
    date = models.DateField()

    def __str__(self):
        return str(self.title)


doctor_group, created = Group.objects.get_or_create(name='Lekarz')
receptionist_group, created = Group.objects.get_or_create(name='Recepcjonista')
patient_group, created = Group.objects.get_or_create(name='Pacjent')
