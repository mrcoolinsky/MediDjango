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
    name = forms.CharField(max_length=20)
    surname = forms.CharField(max_length=20)
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    Street = forms.CharField(max_length=20)
    Number = forms.CharField(max_length=5)
    Zip_code = forms.CharField(max_length=6)
    City = forms.CharField(max_length=20)