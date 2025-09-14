from django import forms

class AnoForm(forms.Form):
    ano = forms.CharField(
        label="Digite o ano",
        max_length=4,
        widget=forms.TextInput(attrs={'placeholder': 'Ex: 1968'})
    )