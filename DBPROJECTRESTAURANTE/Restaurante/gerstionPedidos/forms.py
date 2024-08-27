from django import forms
from .models import Admin,Reserva
from django.shortcuts import redirect
from django import forms

class RegistroUsuario(forms.ModelForm):
    
    class Meta:
        model = Admin
        fields = ['nombre', 'telefono', 'usuario', 'contraseña']
        widgets = {
            'contraseña': forms.PasswordInput(),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        telefono = cleaned_data.get('telefono')
        usuario = cleaned_data.get('usuario')
        contrasena = cleaned_data.get('contraseña')  # Cambiar de 'contraseña' a 'contrasena'
        if Admin.objects.filter(nombre=nombre, telefono=telefono, usuario=usuario, contraseña=contrasena).exists():
            raise forms.ValidationError("¡Esta persona ya está registrada!")
        return cleaned_data

class inicio_sesion(forms.ModelForm):
    
    class Meta:
        model = Admin
        fields = ['usuario', 'contraseña']
        widgets = {
            'contraseña': forms.PasswordInput(),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True

    def clean(self):
        cleaned_data = super().clean()
        usuario = cleaned_data.get('usuario')
        contraseña = cleaned_data.get('contraseña')

        if not Admin.objects.filter(usuario=usuario, contraseña=contraseña).exists():
            raise forms.ValidationError("Credenciales incorrectas. Inténtelo de nuevo.")
        
        return cleaned_data
    
    

class ReservarMesaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['mesa', 'pedido','nombre', 'email', 'telefono', 'fecha']
        widgets = {
            'fecha': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
         
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.required = True

    def save(self, commit=True):
        reserva = super().save(commit=False)
        if commit:
            reserva.save()
            # Obtener la mesa y marcarla como ocupada
            mesa = reserva.mesa
            mesa.estado = True
            mesa.save()
        return reserva