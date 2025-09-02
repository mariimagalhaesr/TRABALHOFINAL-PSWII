from django.db import models
from midia.models import Midia
from denuncia.models import Denuncia

class MidiaDenuncia(models.Model):
    midia = models.ForeignKey(Midia, on_delete=models.CASCADE, related_name="denuncias")
    denuncia = models.ForeignKey(Denuncia, on_delete=models.CASCADE, related_name="midias")