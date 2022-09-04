
from datetime import datetime, timedelta
from django.db import models

from django.db.models import Model


class Rol(models.Model):
    descripcion = models.CharField("Rol", max_length=10, unique=True,null=False)
    def __str__(self):
        return "{0}".format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Rol, self).save()

    class Meta:
        verbose_name_plural = 'Roles'

class Persona(models.Model):
    dni = models.CharField("Cedula", max_length=10,unique=True, null=False)
    nombre = models.CharField("Nombres", max_length= 100, null = False)
    apellido = models.CharField("Apellidos", max_length= 100, null = False)
    telefono = models.CharField("Telefono", max_length=14, null=True)
    email = models.EmailField(null=False, unique=True)
    fecha_registro = models.DateField(auto_now_add=True,null=True)
    rol = models.ForeignKey(Rol, models.CASCADE)
    estado = models.BooleanField(verbose_name='Activo',default=True)



    def save(self):
        self.nombre = self.nombre.upper()
        self.apellido = self.apellido.upper()
        super(Persona, self).save()

class Proveedor(models.Model):
    ruc = models.CharField("R.U.C", max_length=15, null=False, unique=True)
    descripcion = models.CharField("Proveedor", max_length=150, null=False)
    direccion = models.CharField("Direccion", max_length=150, null=False)
    contacto = models.CharField(max_length=150, null=True)
    telefono = models.CharField("Telefono/fax",max_length=15, null=False)
    email = models.EmailField(unique=True, null=False)
    fecha_registro = models.DateField(auto_now_add=True)
    estado = models.BooleanField(default=True,verbose_name='Activo')
    def __str__(self):
        return "{0}".format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        self.contacto = self.contacto.upper()
        super(Proveedor, self).save()

class Producto(models.Model):
    codigo = models.CharField("Codigo producto",max_length=7,unique=True,null=False)
    descripcion = models.CharField("Producto", max_length=100, unique=False, null=False)
    cantidad = models.IntegerField(default=0)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    precio_unitario = models.FloatField(default=0)
    precio_total = models.FloatField(default=0)
    fecha_adquisicion = models.DateField(auto_now_add=True)
    def __str__(self):
        return "{0} ".format(self.descripcion)
    def save(self):
        self.descripcion = self.descripcion.upper()
        self.codigo = self.codigo.upper()
        self.precio_total = self.cantidad * self.precio_unitario
        super(Producto, self).save()


class Bodega(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    SECCION_PRODUCTO =(
        ("LIMPIEZA","limpeza"),
        ("RECOLECCION", "recoleccioin"),
    )
    seccion = models.CharField(max_length=15,choices=SECCION_PRODUCTO,default="RECOLECCION")
    cantidad = models.IntegerField(default=0)
    invercion = models.FloatField(default=0)
    stock = models.IntegerField(default=1)


class Actividad(models.Model):
    actividad = models.CharField("Actividad", max_length=100, unique=True)
    
    def __str__(self):
        return "{0}".format(self.actividad)
    def save(self):
        self.actividad = self.actividad.upper()
        super(Actividad, self).save()

class Cuenta(models.Model):
    empleado = models.ForeignKey(Persona, on_delete=models.CASCADE)
    actividad = models.ForeignKey(Actividad,on_delete=models.CASCADE)
    descripcion = models.CharField("Descripcion", max_length=150, null=False)
    fecha_carga = models.DateField(auto_now_add=True)
    precio = models.FloatField(default=0, null=True)
    estado = models.BooleanField(verbose_name='Activo', default=True)
    producto_cuenta = models.ForeignKey(Producto,  on_delete=models.CASCADE)
    def __str__(self):
        return "{0}".format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()

        super(Cuenta, self).save()

    class Meta:
        verbose_name_plural = "Cuentas"
from datetime import timedelta
class Asistencia(models.Model):
    empleado = models.ForeignKey(Persona, on_delete=models.CASCADE)
    date = models.DateField(("Fecha"), auto_now=True, auto_now_add=False)
    time_in = models.TimeField(("Hora entrada"), auto_now=True, auto_now_add=False, blank = True)
    status = models.BooleanField(("Estado"), default = True)
    time_out = models.TimeField(("Hora salida"), auto_now=True, blank = True)
    def __str__(self):
        return "{0}".format(self.id)

    def save(self,*args, **kwargs):
        return super(Asistencia, self).save()
        
    class Meta:
        verbose_name_plural = "Asistencias"
    
    