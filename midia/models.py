from django.db import models

class Midia(models.Model):
    TIPOS = (
        ('imagem', 'Imagem'),
        ('audio', 'Áudio'),
        ('video', 'Vídeo'),
        ('outro', 'Outro'),
    )

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10, choices=TIPOS)
    arquivo = models.FileField(upload_to="midias/")

    def __str__(self):
        return f"{self.nome} ({self.tipo})"
