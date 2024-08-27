from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField()  # Direcciones de correo electrónico válidas
    telefono = models.CharField(max_length=10)

class Admin(models.Model):
    nombre = models.CharField(max_length=30)
    telefono = models.CharField(max_length=10)
    usuario = models.CharField(max_length=15)
    contraseña = models.CharField(max_length=20)
    

class Reserva(models.Model):
    pedido = models.IntegerField()
    mesa = models.IntegerField()
    nombre = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)
    fecha = models.DateTimeField()
    estado_reserva = models.BooleanField(default=False)

class Menu(models.Model):
    entrada = models.CharField(max_length=15)
    bebida = models.CharField(max_length=15)
    plato = models.CharField(max_length=15)
    precio = models.FloatField()
