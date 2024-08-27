from django.http import HttpResponse
from django.shortcuts import render, redirect
from gerstionPedidos.forms import RegistroUsuario, inicio_sesion, ReservarMesaForm
from gerstionPedidos.models import Admin, Reserva

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
def registro(request):
    if request.method == 'POST':
        form = RegistroUsuario(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Registro exitoso')
    else:
        form = RegistroUsuario()
    return render(request, 'crear_usuario.html', {'formulario': form})

def prueba(request):
    return render(request, 'prueba.html')
    
    
    
def inicio(request):
    accion = request.GET.get('accion')

    if accion == 'login':
        return admin(request)
    elif accion == 'reservar':
        return render(request, 'cliente.html')
    elif accion == 'reservar_mesa':
        return reservar_mesa(request)
    elif accion == 'admin':
        return render(request, 'administrador.html')
    elif accion == 'cliente':
        return render(request, 'cliente.html')
    elif accion == 'crear_usuario':
        return crear_usuario(request)
    elif accion == 'listar_reservas':
        return listar_reservas(request)
    elif accion == 'estado_mesas':
        return estado_mesas(request)
    elif accion == 'inicio_cli':
        return render(request, 'cliente.html')
    elif accion == 'cancelar_reserva':
        return eliminar_reserva(request)
    else:
        return render(request, 'index.html')

def administrador(request):
    return render(request, 'administrador.html')

def crear_usuario(request):
    print("ENTRÓ")
    if request.method == 'POST':
        formulario = RegistroUsuario(request.POST)
        print("FORMULARIO ES VALIDO?")
        if formulario.is_valid():
            print("si")
            formulario.save()
            print("guardo")
            return render(request, 'administrador.html')
        else:
            print("VOLVER")
            return render(request, 'crear_usuario.html', {'formulario': formulario})
    else:
        print("SINO")
        formulario = RegistroUsuario()
        return render(request, 'crear_usuario.html', {'formulario': formulario})

def admin(request):
    accion = request.GET.get('accion')
    if accion == 'login':
        if request.method == 'POST':
            formulario = inicio_sesion(request.POST)
            if formulario.is_valid():
                usuario = formulario.cleaned_data['usuario']
                contrasena = formulario.cleaned_data['contraseña']
                if Admin.objects.filter(usuario=usuario, contraseña=contrasena).exists():
                    return administrador(request)
                else:
                    return render(request, 'inicio.html', {'formulario': formulario, 'error': 'Credenciales inválidas'})
            else:
                return render(request, 'inicio.html', {'formulario': formulario})
        else:
            formulario = inicio_sesion()
            return render(request, 'inicio.html', {'formulario': formulario})
    else:
        return render(request, 'administrador.html')    
    

def reservar_mesa(request):
    if request.method == 'POST':
        formulario = ReservarMesaForm(request.POST)
        if formulario.is_valid():
            mesa_numero = formulario.cleaned_data['mesa']
            if Reserva.objects.filter(mesa=mesa_numero, estado_reserva=True).exists():
                mensaje = "Lo siento, esta mesa está ocupada. Por favor, elija otra mesa."
                request.session['mensaje_reserva'] = mensaje  # Guardar el mensaje en la sesión
                return redirect('reservar_mesa')  # Redireccionar a la misma vista
            else:
                reserva = formulario.save(commit=False)
                reserva.estado_reserva = True
                reserva.save()
                return render(request, 'cliente.html')
    else:
        formulario = ReservarMesaForm()
    
    # Obtener el mensaje de la sesión si existe
    mensaje = request.session.pop('mensaje_reserva', None)
    return render(request, 'reserva.html', {'formulario': formulario, 'mensaje': mensaje})
def listar_reservas(request):
    reservas = Reserva.objects.all() # Cambié "Reserva.object.all()" a "Reserva.objects.all()"
    return render(request, 'listar_reservas.html', {"reservas": reservas})

def eliminar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    reserva.delete()
    return JsonResponse({'message': 'Reserva eliminada correctamente'})



def estado_mesas(request):
    # Obtener todas las reservas
    reservas = Reserva.objects.all()

    # Crear un diccionario para almacenar el estado de cada mesa
    estado_mesas = {}

    # Iterar sobre todas las reservas y actualizar el estado de las mesas en el diccionario
    for reserva in reservas:
        estado_mesas[reserva.mesa] = reserva.estado_reserva

    # Obtener el total de mesas ocupadas
    mesas_ocupadas = sum(estado for estado in estado_mesas.values())

    # Asegurarnos de que haya un tope de 10 mesas
    for mesa in range(1, 13):
        if mesa not in estado_mesas:
            estado_mesas[mesa] = False  # Asignar como disponible

    # Renderizar la plantilla con el estado de las mesas
    return render(request, 'estado_mesas.html', {'estado_mesas': estado_mesas})
