from django.forms import forms as a
from django import forms
from ControlPersonal.models import *


class EmpleadoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['estado'].widget.attrs.update({'class':"form-control"})
        self.fields['telefono'].widget.attrs.update({'placeholder': "telefono"})
        self.fields['email'].widget.attrs.update({'placeholder': "email"})
        self.fields['rol'].empty_label = 'Seleccione rol del empleado'
    class Meta:
        model = Persona
        fields= ['dni', 'nombre', 'apellido',
                 'telefono','email','rol','estado']
        widget = {'nombre': forms.TextInput}

class BodegaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Cuenta
        exclude = ('fecha_carga',)

class ProductoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        
        self.fields['proveedor'].empty_label = 'Seleccione el proveedor'
    class Meta:
        model = Producto
        exclude = ('fecha_adquisicion','precio_total',)
        widget = {'descripcion': forms.TextInput}


class ActividadForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Actividad
        fields = '__all__'
        widget = {'actividad': forms.TextInput}


class CuentaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['estado'].widget.attrs.update({'class':'form-control'})
        self.fields['empleado'].empty_label = 'Seleccione el empleado'
        self.fields['actividad'].empty_label = 'Seleccione la actividdad'
        self.fields['producto_cuenta'].empty_label = 'Seleccione la producto'
        self.fields['descripcion'].widget.attrs.update({'placeholder': "Actividad ha realizar"})
        
    class Meta:
        model = Cuenta
        exclude = ('fecha_carga',)
        widget = {'descripcion': forms.TextInput}

class ProovedorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['estado'].widget.attrs.update({'class': "form-control"})

    class Meta:
        model = Proveedor
        fields = [
            'ruc',
            'descripcion',
            'direccion',
            'contacto',
            'telefono',
            'email',
            'estado']

        labels = {
            'ruc':"Ingrese el ruc",
            'descripcion': "Proovedor",
            'direccion': "Direccion del proovedor",
            'contacto':"Nombre contacto",
            'telefono': "Telefono/fax",
            'correo': "Correo"
        }
        widget = {'descripcion': forms.TextInput}
