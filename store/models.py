from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)
    # Adicione outros campos conforme necessário

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    # Adicione outros campos ao REQUIRED_FIELDS conforme necessário
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
class Tenis(models.Model):
  


    nomeProd = models.CharField(max_length=300, verbose_name='Nome')
    descProd = models.CharField(max_length=300, verbose_name='Deescricao')
    precoProd = models.DecimalField(verbose_name='Preço', max_digits=12, decimal_places=2)
    img1 = models.ImageField()
    img2 = models.ImageField()
    def __str__(self):
        return f'{self.nomeProd}'
