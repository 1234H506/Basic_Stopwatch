from django.db import models

# Create your models here.

class Timer(models.Model):

    class Status(models.TextChoices):
        EM_ANDAMENTO = 'em_andamento', 'Em andamento'
        INTERROMPIDO = 'interrompido', 'Interrompido'
        CONCLUIDO = 'concluido', 'Concluído'

    start = models.DateTimeField()
    vl_pause = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.EM_ANDAMENTO)