from django.db import models

class denuncia(models.Model):
    descricao = models.CharField(max_length=1000)
    envolvidos = models.CharField(max_length=100)
    tipo_abuso = models.CharField(max_length=100)
    provas = models.FileField(
        upload_to='provas/',
        blank=True,
        null=True
    )
    data_acontecimento = models.DateField()
    local = models.CharField(max_length=100)

    def __str__(self):
        return f"Denúncia - {self.tipo_abuso} em {self.local}"
