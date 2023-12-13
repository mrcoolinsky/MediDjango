
from django import forms
from .models import Visit
class AdditionalDataForm(forms.Form):
    title = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    patient = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    doctor = forms.DateField(widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    date = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ['patient_name', 'doctor_name', 'appointment_date']


