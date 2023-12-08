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
    specialization = models.CharField(max_length=50, null=False, default="")

    def __str__(self):
        return str(self.user)


class Medicine(models.Model):
    title = models.CharField(null=False, default="", max_length=20)
    property = models.CharField(null=True, default="", max_length=50)
    availability = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)


class Disease(models.Model):
    title = models.CharField(null=False, default="", max_length=20)
    property = models.CharField(null=False, default="", max_length=50)

    def __str__(self):
        return str(self.title)


class Documentation(models.Model):
    title = models.CharField(max_length=20, null=False, default="")
    patients = models.OneToOneField("Patient", on_delete=models.CASCADE, default="")
    medicines = models.ForeignKey(Medicine, null=True, blank=True, on_delete=models.CASCADE)
    diseases = models.ForeignKey(Disease, null=True, blank=True, on_delete=models.CASCADE)
    visits = models.ForeignKey("Visit", null=True, blank=True, on_delete=models.CASCADE)

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
    patient = models.ForeignKey(Patient, null=False, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, null=False, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return str(self.title)


doctor_group, created = Group.objects.get_or_create(name='Lekarz')
receptionist_group, created = Group.objects.get_or_create(name='Recepcjonista')
patient_group, created = Group.objects.get_or_create(name='Pacjent')
