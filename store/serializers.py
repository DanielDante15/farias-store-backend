from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class TenisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenis
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

