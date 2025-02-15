# Generated by Django 5.0.4 on 2024-04-18 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=10)),
                ('usuario', models.CharField(max_length=15)),
                ('contraseña', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrada', models.CharField(max_length=15)),
                ('bebida', models.CharField(max_length=15)),
                ('plato', models.CharField(max_length=15)),
                ('precio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedido', models.IntegerField()),
                ('mesa', models.IntegerField()),
                ('nombre', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=10)),
                ('fecha', models.DateTimeField()),
            ],
        ),
    ]
