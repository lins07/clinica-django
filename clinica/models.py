from django.db import models
from django.contrib.auth.models import User

class Admin(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    cpf = models.CharField(max_length=11, blank=False) 
    
    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    nome = models.CharField(max_length=50) 
    email = models.EmailField(blank=False)
    cpf = models.CharField(max_length=11, blank=False)
    telefone = models.CharField(max_length=20) 
    curso = models.CharField(max_length=20, blank=False)
    turno = models.CharField(max_length=20)
    sexo  = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=50, blank=False, null=False)
    idade = models.IntegerField(blank=False)
    cpf = models.CharField(max_length=11, blank=False)
    endereco = models.CharField(max_length=100, blank=False)
    sexo = models.CharField(max_length=20, blank=False)
    telefone  = models.CharField(max_length=20) 
    preferencia_de_sexo_para_consulta = models.CharField(max_length=30)
    email = models.EmailField(blank=False)
    horario_da_consulta = models.DateTimeField(blank=False) 
    tipo_de_consulta = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.nome