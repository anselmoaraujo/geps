from django.db import models
from model_utils import Choices

# Criando classe com campos de Docente
class Docente(models.Model):
    objects = None
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    senha = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20, null=True)
    reg_funcional = models.CharField(max_length=100)
    data_cadastro = models.DateTimeField()
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.nome


# Criando uma classe representando a disponibilidade dos Docentes
class DisponibilidadeDocente(models.Model):
    objects = None
    DiaSemana = Choices (
            ('Segunda-Feira'),('Terça-Feira'),('Quarta-Feira'),('Quinta-Feira'),('Sexta-Feira')
        )
    Periodo = Choices (
            ('Manhã'),('Tarde'),('Noite')
        )
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    diaSemana = models.CharField(max_length=20, choices=DiaSemana)
    periodo = models.CharField(max_length=20, choices=Periodo)


# Classe com dos campos da Instituição
class Instituicao(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200, null=True)
    numero = models.CharField(max_length=10, null=True)
    bairro = models.CharField(max_length=50, null=True, default='')
    municipio = models.CharField(max_length=100, null=True)
    estado = models.CharField(max_length=2, null=True)
    cep = models.CharField(max_length=10, null=True)
    email = models.CharField(max_length=150, null=True)
    telefone = models.CharField(max_length=20, null=True)
    nome_responsavel = models.CharField(max_length=100, null=True)
    email_responsavel = models.CharField(max_length=150, null=True)
    telefone_responsavel = models.CharField(max_length=20, null=True)
    senha = models.CharField(max_length=150, default='')

    def __str__(self):
        return self.nome

# Criando uma classe que representa a Demanda por Docentes
class Demanda(models.Model):
    DiaSemana = Choices (
            ('Segunda-Feira'),('Terça-Feira'),('Quarta-Feira'),('Quinta-Feira'),('Sexta-Feira')
        )
    Periodo = Choices (
            ('Manhã'),('Tarde'),('Noite')
        )
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    diaSemana = models.CharField(max_length=20, choices=DiaSemana)
    periodo = models.CharField(max_length=20, choices=Periodo)

# Criando uma classe para os Estados
class Estado(models.Model):
    sigla = models.CharField(max_length=2, null=True)

    def __str__(self):
        return self.sigla

# Criando uma classe para as Cidades
class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name='cidades')

    def __str__(self):
        return self.nome + ' - ' + self.estado.sigla

# Criando uma classe para os Bairros
class Bairro(models.Model):
    nome = models.CharField(max_length=50)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, related_name='bairros')

    def __str__(self):
        return self.nome + ' - ' + self.cidade.nome

    class Meta:
        ordering = ['nome']
