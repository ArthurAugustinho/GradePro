from django.db import models

class Materia(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Periodo(models.Model):
    numero = models.IntegerField(choices=[(i, i) for i in range(1, 9)], default=1)

    def __str__(self):
        return f"Período {self.numero}"

class Ciclo(models.Model):
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    numero = models.IntegerField(null=True)

    def __str__(self):
        return f"Ciclo {self.numero} - {self.periodo}"

class Nota(models.Model):
    materia = models.CharField(max_length=50, default='Valor Padrão')
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE)
    valor = models.FloatField()

    def __str__(self):
        return f"Nota de {self.materia} - {self.ciclo}"

