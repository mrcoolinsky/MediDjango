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
    Name = models.TextField(max_length=20, null=False, default="")
    Surname = models.TextField(max_length=20, null=False, default="")
    Specialization = models.TextField(max_length=50, null=False, default="")

    def __str__(self):
        return str(self.user)
