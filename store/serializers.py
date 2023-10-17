from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'

class TenisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenis
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nome', 'password']

