from django.db import models

# Create your models here.
class consultaClinica(models.Model):
    nome = models.CharField(max_length=200)
    sobreNome = models.CharField(max_length=200)
    datadeNascimento = models.DateField()
    cpf = models.CharField(max_length=11)
    Endereço = models.CharField(max_length=200)
    Bairro = models.CharField(max_length=200)
    Cidade = models.CharField(max_length=200)
    Cep = models.CharField(max_length=200)
    sus = models.CharField(max_length=15)
    telefone = models.CharField(max_length=200)
    email = models.EmailField()