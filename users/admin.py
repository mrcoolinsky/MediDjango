from django.contrib import admin
from main.models import Doctor, Patient, Visit, Medicine, Disease, Address, Dosage

# Register your models here.

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Visit)
admin.site.register(Medicine)
admin.site.register(Disease)
admin.site.register(Address)
admin.site.register(Dosage)