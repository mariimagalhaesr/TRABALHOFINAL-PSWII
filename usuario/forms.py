from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm

class UsuarioForm(UserCreationForm):
    first_name = forms.CharField(max_length=150, required=True, label="Nome Completo")
    email = forms.EmailField(max_length=254, required=False, label="E-mail")
    cpf = forms.CharField(max_length=14, required=True)
    setor = forms.ChoiceField(choices=Usuario.SETOR_CHOICES, required=True)

    class Meta(UserCreationForm.Meta):
        model = Usuario
        fields = ['first_name', 'username', 'email', 'cpf', 'setor', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        

class UsuarioEditForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'username', 'email', 'cpf', 'setor']
        labels = {
            'first_name': 'Nome Completo',
            'username': 'Nome de Usuário',
            'email': 'E-mail',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '000.000.000-00'}),
            'setor': forms.Select(attrs={'class': 'form-control'}),
        }