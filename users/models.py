from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    Street = models.TextField()
    Number = models.TextField()
    Zip_code = models.TextField()
    City = models.TextField()


class Doctor(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    address = models.OneToOneField(Address, null=False, on_delete=models.CASCADE, default="")
    Name = models.CharField(max_length=20, null=False, default="")
    Surname = models.CharField(max_length=20, null=False, default="")
    Specialization = models.CharField(max_length=50, null=False, default="")

    def __str__(self):
        return str(self.user)


class Medicine(models.Model):
    title = models.CharField(null=False, default="", max_length=20)
    property = models.CharField(null=True, default="", max_length=50)
    availability = models.BooleanField(default=False)


class Disease(models.Model):
    title = models.CharField(null=False, default="", max_length=20)
    property = models.CharField(null=True, default="", max_length=50)

class Documentation(models.Model):
    medicines = models.ManyToManyField(Medicine)
    diseases = models.ManyToManyField(Disease)
    visits = models.ManyToManyField(Visit)

class Patient(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    address = models.OneToOneField(Address, null=False, on_delete=models.CASCADE, default="")
    Name = models.CharField(max_length=20, null=False, default="")
    Surname = models.CharField(max_length=20, null=False, default="")
    DateOfBirth = models.DateField(max_length=10, null=False, default="")
    Documentation = models.OneToOneField(Documentation, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)

class Visit(models.Model):
    title = models.CharField(null=False, default="", max_length=20)
    patient = models.OneToOneField(Patient, null=False, on_delete=models.CASCADE)
    doctor = models.OneToOneField(Doctor, null=False, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return str(self.title)






