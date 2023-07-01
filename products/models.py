from django.db import models
from datetime import datetime
import pytz

class Vendedor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    setores = models.ManyToManyField('Setor')
    foto_perfil = models.URLField(blank=True, null=True)
    horario_abertura = models.TimeField()
    horario_fechamento = models.TimeField()

    @property
    def status(self):
        fuso_horario = pytz.timezone('America/Sao_Paulo')
        now = datetime.now(fuso_horario).time()
        if self.horario_abertura <= now < self.horario_fechamento:
            return 'Disponível'
        else:
            return 'Indisponível'


    def __str__(self):
        return self.nome

class Setor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.CharField(max_length=100)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
