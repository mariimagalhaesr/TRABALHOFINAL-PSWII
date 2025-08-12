from django import forms
from .models import Denuncia

class DenunciaForm(forms.ModelForm):
    data_acontecimento = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs={'placeholder': 'dd/mm/aaaa'}
        )
    )

    class Meta:
        model = Denuncia
        fields = '__all__'

    def clean_provas(self):
        arquivo = self.cleaned_data.get('provas')
        if arquivo:
            tipo = arquivo.content_type
            if not any([
                tipo.startswith('image/'),
                tipo.startswith('video/'),
                tipo.startswith('audio/')
            ]):
                raise forms.ValidationError("O arquivo deve ser uma imagem, vídeo ou áudio.")
        return arquivo
