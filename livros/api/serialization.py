from rest_framework import serializers
from .models import *

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ('titulo', 'autor', 'volume', 'versao', 'codigo')

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ('titulo', 'autor', 'volume', 'versao', 'codigo')
