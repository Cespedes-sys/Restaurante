from django.contrib import admin
from django.urls import path
from Restaurante.views import inicio, registro, administrador, crear_usuario, reservar_mesa, listar_reservas,eliminar_reserva,prueba

urlpatterns = [
    path('administrador/', administrador),
    path('crear_usuario/', crear_usuario),
    path('inicio/', inicio),
    path('prueba/', prueba),
    path('registro/', registro),
    path('reservar_mesa/', reservar_mesa, name='reservar_mesa'),
    path('listar_reservas/', listar_reservas, name='listar_reservas'),
    path('eliminar-reserva/<int:reserva_id>/', eliminar_reserva, name='eliminar_reserva'),
    
    
]



