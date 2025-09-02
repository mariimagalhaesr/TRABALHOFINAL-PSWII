from django.db import models
from django.contrib.auth.models import User

class Usuario(User):

    cpf = models.CharField(max_length=14, unique=True)
    setor = models.CharField(max_length=100)

    def __str__(self):

        return self.get_full_name() or self.username