from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.forms.widgets import PasswordInput, TextInput


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


class AdditionalDataForm(forms.Form):
    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    surname = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    street = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    number = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'class': 'form-control'}))
    zip_code = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))

class MakeAppointmentForm(forms.Form):
    first_name = forms.CharField(label='Imię pacjenta', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Nazwisko pacjenta', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    appointment_date = forms.DateTimeField(label='Data wizyty', widget=forms.TextInput(attrs={'type': 'datetime-local', 'class': 'form-control'}))
    doctor_name = forms.CharField(label='Imię doktora', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))


