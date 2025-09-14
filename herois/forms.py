
from django import forms

from .models import HeroiModel

class HeroiForm(forms.ModelForm):
    class Meta:
        model = HeroiModel
        fields = ['nome']