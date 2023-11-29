from rest_framework.viewsets import *
from rest_framework.status import *
from .serializers import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json


@csrf_exempt
@require_POST
def validate_user(request):
    data = json.loads(request.body)
    username = data.get('username', '')
    password = data.get('password', '')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        return JsonResponse({'valid': True})
    else:
        return JsonResponse({'valid': False})



class TenisAPIView(ModelViewSet):
    queryset = Tenis.objects.all()
    serializer_class = TenisSerializer

class UsuarioAPIView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
