from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.forms.widgets import PasswordInput, TextInput
from main.models import Patient, Address, Doctor, Visit, Disease, Dosage


# create/register user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


# login user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class PatientDataForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))

    class Meta:
        model = Patient
        fields = ['name', 'surname', 'date_of_birth', 'phone_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class DoctorDataForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'surname', 'specialization', 'phone_number']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class AddressDataForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'number', 'zip_code', 'city']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class VisitDataForm(forms.ModelForm):
    date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))

    class Meta:
        model = Visit
        fields = ['title', 'doctor', 'date', 'notes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class DiseaseDataForm(forms.ModelForm):
    class Meta:
        model = Disease
        fields = ['title', 'symptoms']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class DosageDataForm(forms.ModelForm):
    class Meta:
        model = Dosage
        fields = ['start_date', 'end_date', 'medicine', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'