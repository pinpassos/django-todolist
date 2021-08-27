from django.db import models


# Create your models here.
class Tarefas(models.Model):
    tarefa_texto = models.CharField(max_length=100)
    descricao_texto = models.CharField(max_length=300)
    importancia = models.BooleanField()

    def __str__(self):
        return self.tarefa_texto
