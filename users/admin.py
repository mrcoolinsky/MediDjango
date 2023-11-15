from django.contrib import admin
from .models import Doctor, Patient, Visit, Documentation, Medicine, Disease, Address
# Register your models here.

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Visit)
admin.site.register(Documentation)
admin.site.register(Medicine)
admin.site.register(Disease)
admin.site.register(Address)