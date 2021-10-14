from django.forms import fields
from .models import todo
from django import forms


class todoform(forms.ModelForm):
    class Meta:
        model = todo
        exclude = ['peserta']

