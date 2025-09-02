from django import forms
from .models import Midia

class MidiaForm(forms.ModelForm):
    class Meta:
        model = Midia
        fields = ['nome', 'tipo', 'arquivo']
        labels = {
            'nome': 'Nome da Mídia',
            'tipo': 'Tipo de Mídia',
            'arquivo': 'Arquivo',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'arquivo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
