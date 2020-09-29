from django import forms
from .models import *
from django.forms import ModelForm

class taskForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new Task...'}))
    class Meta:
        model = task
        fields = '__all__'
