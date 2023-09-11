from .views import *
from rest_framework_nested import routers
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()

router.register('enderecos', EnderecoAPIView, basename='enderecos')
router.register('tenis', TenisAPIView, basename='tenis')
router.register('usuarios', UsuarioAPIView, basename='usuarios')

urlpatterns = router.urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)