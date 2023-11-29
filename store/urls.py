from .views import TenisAPIView, UsuarioAPIView, validate_user
from rest_framework_nested import routers
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

router = routers.DefaultRouter()

router.register('tenis', TenisAPIView, basename='tenis')
router.register('usuarios', UsuarioAPIView, basename='usuarios')

urlpatterns = [
    path('login/', validate_user, name='login'),
    # Adicione outras URLs conforme necessário
]

# Adicione as URLs do router às URLs existentes
urlpatterns += router.urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
