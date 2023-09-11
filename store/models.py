from django.db import models
from django.contrib.auth.models import User

class Tenis(models.Model):


    MARCAS_TENIS = [
    ('Nike', 'Nike'),
    ('Adidas', 'Adidas'),
    ('Puma', 'Puma'),
    ('New Balance', 'New Balance'),
    ('Asics', 'Asics'),
]

    TAMANHO_CHOICES = [
    ('34', '34'),
    ('35', '35'),
    ('36', '36'),
    ('37', '37'),
    ('38', '38'),
    ('39', '39'),
    ('40', '40'),
    ('41', '41'),
    ('42', '42'),
    ('43', '43'),
    ('44', '44'),
]
    imagem = models.ImageField()
    marca = models.CharField(max_length=20,choices=MARCAS_TENIS,verbose_name='Marca')
    modelo = models.CharField(max_length=50,verbose_name='Modelo')
    preco = models.DecimalField(verbose_name='Preço',max_digits=12,decimal_places=2)
    tamanho = models.CharField(max_length=2, choices=TAMANHO_CHOICES,verbose_name='Tamanho')

    def __str__(self):
        return self.marca +' '+self.modelo




class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        # Calcula o total do pedido somando o subtotal de todos os itens do pedido
        return sum(item.subtotal for item in self.itens.all())
    
    def __str__(self):
        
        return f'Pedido #{self.pk} - {self.usuario.username}'

class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    tenis = models.ForeignKey(Tenis, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    
    def subtotal(self):

        print('oiiiiiii')
        return self.quantidade * self.preco_unitario
    
    def __str__(self):
        return f'Item do Pedido #{self.pedido.pk} - {self.tenis.marca}'


class Endereco(models.Model):
    customer = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True,verbose_name='Cliente')
    order = models.ForeignKey(Pedido,on_delete=models.SET_NULL,blank=True,null=True,verbose_name='Pedido')
    address = models.CharField(max_length=200,null=True,verbose_name='Logradouro')
    city = models.CharField(max_length=200,null=True,verbose_name='Cidade')
    state = models.CharField(max_length=200,null=True,verbose_name='Estado')
    zip_code = models.CharField(max_length=200,null=True,verbose_name='CEP')

    def __str__(self):
        return self.address