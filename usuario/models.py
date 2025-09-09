from django.db import models
from django.contrib.auth.models import User, Group

class Usuario(User):
    SETOR_CHOICES = (
        ('CA', 'Coordenação de Ensino'),
        ('CAE', 'Coordenação de Assuntos Estudantis'),
        ('Diretoria Academica', 'Diretoria Acadêmica'),
        ('Administrativo', 'Administrativo'),
        ('NAPNE', 'Núcleo de Atendimento a Pessoas com Necessidades Específicas'),
        ('Outro', 'Outro'),
    )
    
    cpf = models.CharField(max_length=14, unique=True)
    setor = models.CharField(choices=SETOR_CHOICES, max_length=100, default='OUT')

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        setor_label = dict(self.SETOR_CHOICES).get(self.setor, 'Outro')
        grupo, _ = Group.objects.get_or_create(name=setor_label)

        self.groups.clear()
        self.groups.add(grupo)

    def __str__(self):
        return self.get_full_name() or self.username

    