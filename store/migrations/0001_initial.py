# Generated by Django 4.1.7 on 2023-09-06 00:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pedido', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False, null=True, verbose_name='Finalizado')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tenis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='')),
                ('marca', models.CharField(choices=[('Nike', 'Nike'), ('Adidas', 'Adidas'), ('Puma', 'Puma'), ('New Balance', 'New Balance'), ('Asics', 'Asics')], max_length=20, verbose_name='Marca')),
                ('modelo', models.CharField(max_length=50, verbose_name='Modelo')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Preço')),
                ('tamanho', models.CharField(choices=[('34', '34'), ('35', '35'), ('36', '36'), ('37', '37'), ('38', '38'), ('39', '39'), ('40', '40'), ('41', '41'), ('42', '42'), ('43', '43'), ('44', '44')], max_length=2, verbose_name='Tamanho')),
            ],
        ),
        migrations.CreateModel(
            name='PedidoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('data_pedido', models.DateTimeField(auto_now_add=True)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.pedido')),
                ('tenis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.tenis', verbose_name='Tenis')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, null=True, verbose_name='Logradouro')),
                ('city', models.CharField(max_length=200, null=True, verbose_name='Cidade')),
                ('state', models.CharField(max_length=200, null=True, verbose_name='Estado')),
                ('zip_code', models.CharField(max_length=200, null=True, verbose_name='CEP')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Cliente')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.pedido', verbose_name='Pedido')),
            ],
        ),
    ]
