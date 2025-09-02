from django import forms
from .models import Denuncia

class DenunciaAnonimaForm(forms.ModelForm):

    arquivos_prova = forms.FileField(
        required=False,
        label="Anexar Provas (Imagens, Vídeos, Documentos)"
    )

    class Meta:
        model = Denuncia
        fields = ['descricao', 'dt_ocorrido', 'categoria', 'local', 'envolvidos']
        labels = {
            'descricao': 'Descrição',
            'dt_ocorrido': 'Data do Ocorrido',
            'categoria': 'Categoria',
            'local': 'Local',
            'envolvidos': 'Envolvidos',
        }
        widgets = {
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'dt_ocorrido': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'local': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Laboratório de Informática'}),
            'envolvidos': forms.TextInput(attrs={'class': 'form-control'}),
        }

class DenunciaStatusForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = ['status', 'dt_fim', 'desfecho', 'recebido_por', 'finalizado_por']
        labels = {
            'status': 'Status da Denúncia',
            'dt_fim': 'Data de Finalização',
        }
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control' }),
            'dt_fim': forms.DateInput(attrs={'type': 'date', 'required': False, 'class': 'form-control'}),
            'desfecho': forms.Textarea(attrs={'rows': 2, 'required': False, 'class': 'form-control'}),
            'recebido_por': forms.Select(attrs={'class': 'form-control'}),
            'finalizado_por': forms.Select(attrs={'class': 'form-control', 'required': False}),
        }

class ConsultaStatusForm(forms.Form):
    codigo = forms.CharField(
        label="Código de Rastreamento",
        max_length=32,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cole o seu código aqui'})
    )
    