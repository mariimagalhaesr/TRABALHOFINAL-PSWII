from django import forms
from .models import Categoria

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ['nome']
        labels = {
            'nome': 'Nome da Categoria',
        }
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
        }