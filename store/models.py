from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.utils import timezone

class UsuarioManager(BaseUserManager):
    def create_user(self, nome, senha=None, endereco=None):
        if not nome:
            raise ValueError('O nome de usuário é obrigatório')
        
        usuario = self.model(
            nome=nome,
            endereco=endereco,
        )

        usuario.set_password(senha)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, nome, senha=None, endereco=None):
        usuario = self.create_user(
            nome=nome,
            senha=senha,
            endereco=endereco,
        )
        usuario.is_staff = True
        usuario.is_superuser = True
        usuario.save(using=self._db)
        return usuario

class Usuario(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    groups = models.ManyToManyField(Group, related_name='usuarios')
    user_permissions = models.ManyToManyField(Permission, related_name='usuarios_permissoes')
    objects = UsuarioManager()

    USERNAME_FIELD = 'nome'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.nome

class Tenis(models.Model):
  


    nomeProd = models.CharField(max_length=300, verbose_name='Nome')
    descProd = models.CharField(max_length=300, verbose_name='Modelo')
    precoProd = models.DecimalField(verbose_name='Preço', max_digits=12, decimal_places=2)
    img1 = models.ImageField()
    img2 = models.ImageField()
    def __str__(self):
        return f'{self.nomeProd}'

class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        return sum(item.subtotal for item in self.itens.all())
    
    def __str__(self):
        return f'Pedido #{self.pk} - {self.usuario.nome}'

class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    tenis = models.ForeignKey(Tenis, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    
    @property
    def subtotal(self):
        return self.quantidade * self.tenis.precoProd
    
    def __str__(self):
        return f'Item do Pedido #{self.pedido.pk} - {self.tenis.nomeProd}'

class Endereco(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, blank=True, null=True,verbose_name='Cliente')
    logradouro = models.CharField(max_length=200, null=True, verbose_name='Logradouro')
    cidade = models.CharField(max_length=200, null=True, verbose_name='Cidade')
    estado = models.CharField(max_length=200, null=True, verbose_name='Estado')
    cep = models.CharField(max_length=200, null=True, verbose_name='CEP')

    def __str__(self):
        return self.logradouro
