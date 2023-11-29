from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.forms.widgets import PasswordInput, TextInput


# create/register user
class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    date_of_birth = forms.DateField()
    """
    Street = forms.CharField()
    Number = forms.CharField()
    Zip_code = forms.CharField()
    City = forms.CharField()
    'Street', 'Number', 'Zip_code', 'City',
"""
    class Meta:
        model = User
        fields = (
            "username", 'email', 'first_name', 'last_name', 'date_of_birth',
            'password1', 'password2')


# login user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
