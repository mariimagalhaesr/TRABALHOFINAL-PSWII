from django.db import models
from categoria.models import Categoria
from usuario.models import Usuario
import uuid


class Denuncia(models.Model):
    STATUS_CHOICES = (
        ('recebida', 'Recebida'),
        ('em_andamento', 'Em Andamento'),
        ('finalizada', 'Finalizada'),
        ('arquivada', 'Arquivada'),
    )

    descricao = models.TextField()
    dt_envio = models.DateTimeField(auto_now_add=True)
    codigo_rastreamento = models.CharField(max_length=32, unique=True, blank=True, editable=False, help_text="Código único para o denunciante acompanhar o status.")    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='nova')
    dt_ocorrido = models.DateTimeField(verbose_name="Data e Hora do Ocorrido")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="denuncias")
    local = models.CharField(max_length=255)
    dt_fim = models.DateField(null=True, blank=True)
    envolvidos = models.TextField(blank=True, null=True, help_text="Descreva os envolvidos na denúncia, se houver.")
    desfecho = models.TextField(blank=True, null=True)
    recebido_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, blank=True, null=True, related_name="denuncias_recebidas")
    finalizado_por = models.ForeignKey(Usuario, on_delete=models.SET_NULL, blank=True, null=True, related_name="denuncias_finalizadas")

    def save(self, *args, **kwargs):

        if not self.codigo_rastreamento:
            self.codigo_rastreamento = uuid.uuid4().hex
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Denúncia #{self.id} - {self.categoria.nome}"

