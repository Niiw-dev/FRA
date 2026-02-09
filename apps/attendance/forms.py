from django import forms
from .models import Fingerprint

class FingerprintForm(forms.ModelForm):
    class Meta:
        model = Fingerprint
        fields = ['fingerprint_uid', 'full_name', 'is_active']
        widgets = {
            'fingerprint_uid': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'UID de la huella'
            }),
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre completo'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'centerIsActive',
            }),
        }
