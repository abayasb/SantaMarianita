from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.base import View

from ControlPersonal.forms import *
from ControlPersonal.models import *

from django.core import serializers


@login_required(login_url='/login/')
def Homes(request):
    persona = Persona.objects.all()
    data = {
        'persona':persona
    }
    return render(request,"table/home.html",data)

class Home(LoginRequiredMixin,generic.ListView):
    template_name = "table/home.html"
    login_url = 'ControlPersonal:login'
    def get(self, request, *args, **kwargs):
        empledo = Persona.objects.all()
        egreso_producto = Producto.objects.aggregate(Sum('precio_total'))
        cantidad_producto = Producto.objects.all()
        cantidad_producto = cantidad_producto.count()
        egreso_empleado = Cuenta.objects.aggregate(Sum('precio'))
        data = {
            'empleado':empledo,
            'egreso_empleado':egreso_empleado['precio__sum'],
            'egreso_producto':egreso_producto['precio_total__sum'],
            'cantidad_producto':cantidad_producto
        }
        print(cantidad_producto)
        return render(request,self.template_name,data)

##APARTADO PARA REALIZAR EL C.R.U.D  de empleado
class EmpleadoListView(LoginRequiredMixin,generic.ListView):
    model = Persona
    template_name = "table/empleado.html"
    context_object_name = 'object'
    login_url = "ControlPersonal:login"


class EmpleadoCreateView(LoginRequiredMixin, generic.CreateView):
    model = Persona
    template_name = "forms/empleado.html"
    context_object_name = 'object'
    success_url = reverse_lazy("ControlPersonal:lista_empleado")
    form_class = EmpleadoForm
    login_url = "ControlPersonal:login"
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class EmpleadoUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Persona
    template_name = "forms/empleado.html"
    context_object_name = 'object'
    success_url = reverse_lazy("ControlPersonal:lista_empleado")
    form_class = EmpleadoForm
    login_url = "ControlPersonal:login"

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

@login_required(login_url='/login/')
def inavilitarEmpleado(request, id):
    template_name = 'inactivar/empleado.html'
    empleado = Persona.objects.filter(pk=id).first()
    context = {}
    if not empleado:
        return HttpResponse("Empleado no existe")
    if request.method == 'GET':
        context={'empleado':empleado}

    if request.method == 'POST':
        empleado.estado = False
        empleado.save()
        context = {'empleado':'POSITIVO'}
        return HttpResponse("Empleado Inactivo")

    return render(request,template_name,context)

##APARTADO PARA REALIZAR EL C.R.U.D  de proveedor
class ProovedorViewList(LoginRequiredMixin, generic.ListView):
    model = Proveedor
    template_name = 'table/proveedor.html'
    context_object_name = "object"
    login_url = 'ControlPersonal:login'

class ProovedorView(LoginRequiredMixin, generic.CreateView):
    model = Proveedor
    template_name = 'forms/proveedor.html'
    form_class = ProovedorForm
    success_url = reverse_lazy('ControlPersonal:lista_proovedor')
    login_url = 'ControlPersonal:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class ProovedorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Proveedor
    template_name = "forms/proveedor.html"
    form_class = ProovedorForm
    success_url = reverse_lazy('ControlPersonal:lista_proovedor')
    login_url = 'ControlPersonal:login'
    def form_valid(self, form):
        form.instance.um = self.request.user
        return super().form_valid(form)

def inavilitarProovedor(request, id):
    template_name = 'inactivar/proveedor.html'
    proovedor = Proveedor.objects.filter(pk = id).first()
    context = {}
    if not proovedor:
        return HttpResponse('Proovedor no existe'+str(id))

    if request.method == 'GET':
        context = {
            'proovedor':proovedor
        }

    if request.method == 'POST': ## SE EJECUTA CUANDO SE LE DA AL BOTON DE ENVIAR
        proovedor.estado = False
        proovedor.save()
        context = {
            'proovedor':'POSITIVO'
        }
        return HttpResponse('Proovedor Inactivado')
    return render(request,template_name,context)

##APARTADO PARA REALIZAR EL C.R.U.C de producto.
class ProductoViewList(LoginRequiredMixin, generic.ListView):
    model = Producto
    template_name = 'table/producto.html'
    context_object_name = 'object'
    login_url = 'ControlPersonal:login'

class ProductoCreateView(LoginRequiredMixin, generic.CreateView):
    model = Producto
    template_name = 'forms/producto.html'
    form_class = ProductoForm
    context_object_name = 'object'
    success_url = reverse_lazy("ControlPersonal:lista_producto")
    login_url = 'ControlPersonal:login'

    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super().form_valid(form)

class ProductoUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Producto
    template_name = 'forms/producto.html'
    form_class = ProductoForm
    context_object_name = 'object'
    success_url = reverse_lazy("ControlPersonal:lista_producto")
    login_url = 'ControlPersonal:login'

    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super().form_valid(form)

##APARTADO PARA REALIZAR EL C.R.U.C de producto bodega
class ProductoBodegaViewList(LoginRequiredMixin, generic.ListView):
    model = Bodega
    template_name = "table/bodega.html"
    context_object_name = 'object'
    login_url = 'ControlPersonal:login'

##class ProductoBodegaCreateView(LoginRequiredMixin, generic.CreateView):
##    def post(self, request, *args, **kwargs):


##APARTADO PARA LA REALIZACION DEL C.R.U.D de cuenta
class CuentaListView(LoginRequiredMixin,generic.ListView):
    model = Cuenta
    template_name = "table/cuenta.html"
    login_url = "ControlPersonal:login"
    context_object_name = 'object'

class CuentaCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cuenta
    template_name = "forms/cuenta.html"
    form_class = CuentaForm
    context_object_name = 'object'
    success_url = reverse_lazy("ControlPersonal:lista_cuenta")
    login_url = "ControlPersonal:login"
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super(CuentaCreateView, self).form_valid(form)

class CuentaUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cuenta
    template_name = "forms/cuenta.html"
    form_class = CuentaForm
    context_object_name = 'object'
    success_url = reverse_lazy("ControlPersonal:lista_cuenta")
    login_url = "ControlPersonal:login"
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super(CuentaUpdateView, self).form_valid(form)


##APARADO PARA LAS ACTIVIDADES
class ActividadListView(LoginRequiredMixin,generic.ListView):
    model = Actividad
    template_name = "table/actividad.html"
    context_object_name = 'object'
    login_url = "ControlPersonal:login"

class ActividadCreateView(LoginRequiredMixin, generic.CreateView):
    model = Actividad
    template_name = "forms/actividad.html"
    context_object_name = 'object'
    success_url = reverse_lazy("ControlPersonal:lista_actividad")
    form_class = ActividadForm
    login_url = "ControlPersonal:login"
    def form_valid(self, form):
        form.instance.uc = self.request.user
        return super(ActividadCreateView, self).form_valid(form)

class ActividadUpdateView(LoginRequiredMixin,generic.UpdateView):
    model = Actividad
    template_name = "forms/actividad.html"
    context_object_name = 'object'
    success_url = reverse_lazy("ControlPersonal:lista_actividad")
    form_class = ActividadForm
    login_url = "ControlPersonal:login"
    def form_valid(self, form):
        form.instance.um = self.request.user.id
        return super(ActividadUpdateView, self).form_valid(form)

class AsistenciaListView(LoginRequiredMixin, generic.ListView):
    model = Asistencia
    template_name = "table/asistencia.html"
    context_object_name = 'object'
    login_url = 'ControlPersonal:login'
   

class RegistroAsistencia(LoginRequiredMixin,generic.CreateView):
    model = Asistencia
    form_class = AsistenciaForm
    login_url = "ControlPersonal:login"
    success_url = reverse_lazy("ControlPersonal:lista_cuenta")
    def post(self, request, *args, **kwargs):
        a = request.POST['cedula']
        empleado = Persona.objects.filter(dni=a).first()
        asistencia = Asistencia(empleado=empleado)
        asistencia.save()
        return HttpResponse()

       