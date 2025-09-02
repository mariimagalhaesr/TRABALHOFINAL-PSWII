from django.db import models
from denuncia.models import Denuncia
from midia.models import Midia

class MidiaDenuncia(models.Model):
    denuncia = models.ForeignKey(Denuncia, on_delete=models.CASCADE, related_name="provas")
    midia = models.ForeignKey(Midia, on_delete=models.CASCADE)
    conteudo = models.FileField(upload_to="provas_denuncias/")

    def __str__(self):
        return f"Prova para a Denúncia #{self.denuncia.id}"