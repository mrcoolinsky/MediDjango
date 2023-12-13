from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.forms.widgets import PasswordInput, TextInput
from main.models import Patient, Address, Doctor


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

class MakeAppointmentForm(forms.Form):
    first_name = forms.CharField(label='Imię pacjenta', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Nazwisko pacjenta', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    appointment_date = forms.DateTimeField(label='Data wizyty', widget=forms.TextInput(attrs={'type': 'datetime-local', 'class': 'form-control'}))
    doctor_name = forms.CharField(label='Imię doktora', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))


