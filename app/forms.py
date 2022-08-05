from django import forms
from .models import Movies
class EditForm(forms.ModelForm):
    class Meta:
        model=Movies
        fields=['name','img','des','year']