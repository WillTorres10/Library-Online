from rest_framework import serializers
from .models import *

class EstudanteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estudante
        fields = ('first_name', 'last_name', 'email', 'matricula')
