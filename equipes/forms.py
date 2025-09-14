from django import forms
from .models import EquipeModel

class EquipeForm(forms.ModelForm):
    class Meta:
        model = EquipeModel
        fields = ['nome', 'membros']

