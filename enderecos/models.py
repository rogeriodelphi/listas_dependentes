from django.db import models

class Estado(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Cidade(models.Model):
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True, blank=True)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome