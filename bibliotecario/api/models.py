from django.db import models

# Create your models here.

class recuperarSenha(models.Model):
    token = models.CharField(max_length=256)
    emailUser = models.CharField(max_length=40)
