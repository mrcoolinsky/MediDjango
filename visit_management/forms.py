from django import forms
class AdditionalDataForm(forms.Form):
    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    surname = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_of_birth = forms.DateField(widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))
    street = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    number = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'class': 'form-control'}))
    zip_code = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))