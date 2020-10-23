from django.db import models


class Estado(models.Model):
    nome = models.CharField(max_length=30)
    uf = models.CharField(max_length=2, null=False ,verbose_name='UF')

    def __str__(self):
        return self.nome


class Cidade(models.Model):
#    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    uf = models.ForeignKey(Estado, max_length=2, on_delete=models.PROTECT, verbose_name='uf')
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True, blank=True)
    uf = models.ForeignKey(Estado, on_delete=models.SET_NULL, null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome