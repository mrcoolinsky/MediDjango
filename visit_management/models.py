from django.db import models

# Create your models here.
class Visit(models.Model):
    title = models.CharField(null=False, default="", max_length=20)
    patient = models.ForeignKey("Patient", null=False, on_delete=models.CASCADE)
    doctor = models.ForeignKey("Doctor", null=False, on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return str(self.title)

