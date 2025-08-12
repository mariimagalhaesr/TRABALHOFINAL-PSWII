from django.db import models
from categoria.models import Categoria
import uuid

class DescricaoDenuncia(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    data_ocorrido = models.DateTimeField()
    descricao = models.TextField()
    envolvidos = models.CharField(max_length=255, blank=True)
    local_ocorrido = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao

class Denuncia(models.Model):
    STATUS_CHOICES = (
        ('nova', 'Nova'),
        ('em_andamento', 'Em Andamento'),
        ('finalizada', 'Finalizada'),
        ('arquivada', 'Arquivada'),
    )
    data_envio = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='nova')
    usuario_anonimo = models.CharField(max_length=100, blank=True, null=True, help_text="Preencha se a denúncia for anônima")
    descricao_denuncia = models.OneToOneField(DescricaoDenuncia, on_delete=models.CASCADE)
    data_cancelamento = models.DateTimeField(null=True, blank=True)
    data_finalizacao = models.DateTimeField(null=True, blank=True)
    codigo_acompanhamento = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, null=True)

    def __str__(self):
        return f"Denúncia #{self.pk} - {self.status}"
    
class TipoProva(models.Model):
    audio = models.FileField(upload_to='provas/audios/', null=True, blank=True)
    foto = models.ImageField(upload_to='provas/fotos/', null=True, blank=True)
    video = models.FileField(upload_to='provas/videos/', null=True, blank=True)
    denuncia = models.ForeignKey('Denuncia', on_delete=models.CASCADE, related_name='provas')

    def __str__(self):
        return f"Prova para Denúncia #{self.denuncia.id}"
