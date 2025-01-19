from django import forms
from main.models import Visit, Disease, Dosage

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = ("title", 'patient', 'doctor', 'notes', 'date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class VisitAddForm(forms.ModelForm):
    date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date', 'class': 'form-control'}))

    class Meta:
        model = Visit
        fields = ['title','patient' ,'doctor', 'date', 'notes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'