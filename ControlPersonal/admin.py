from django.contrib import admin

# Register your models here.
from ControlPersonal.models import *
admin.site.register(Rol)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Actividad)
admin.site.register(Persona)
admin.site.register(Cuenta)
admin.site.register(Asistencia)