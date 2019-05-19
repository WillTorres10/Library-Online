from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    volume = models.CharField(max_length=50)
    versao = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50, unique=True)

class EmprestarLivro(models.Model):
    codigoLivro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    matriculaLivro = models.CharField(max_length=15)
    alugado = models.BooleanField(default=False)