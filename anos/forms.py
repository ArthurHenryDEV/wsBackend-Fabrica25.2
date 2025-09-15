from django import forms

from . models import AnoModel

class AnoForm(forms.ModelForm):
    class Meta:
        model = AnoModel
        fields = ['ano']
      