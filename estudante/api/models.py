from django.db import models
from django.contrib.auth.models import User

class Estudante(User):
    matricula = models.CharField(max_length=15)
