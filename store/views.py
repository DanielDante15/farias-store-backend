from rest_framework.viewsets import *
from rest_framework.status import *
from .serializers import *
from django.contrib.auth.models import User


class TenisAPIView(ModelViewSet):
    queryset = Tenis.objects.all()
    serializer_class = TenisSerializer

class EnderecoAPIView(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class UsuarioAPIView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
