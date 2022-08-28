from sys import path

from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .views import *

urlpatterns = [
    #path('', views.Homes, name="home"),
    path('',Home.as_view(), name= "home"),
    path('login/', auth_views.LoginView.as_view(template_name='bases/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='bases/login.html'), name='logout'),
    #URL PARA LA SECCION DE EMPLEADOS
    path("empleado/", EmpleadoListView.as_view(), name="lista_empleado"),
    path("empleado/nuevo", EmpleadoCreateView.as_view(), name="nuevo_empleado"),
    path("empleado/editar/<int:pk>", EmpleadoUpdateView.as_view(), name="editar_empleado"),
    path("empleado/delete/<int:id>", inavilitarEmpleado, name="delete_empleado"),

    #URL PARA LA SECCION DE PROVEEDORES
    path('proveedor/',ProovedorViewList.as_view(), name ='lista_proovedor'),
    path("proveedor/nuevo",ProovedorView.as_view(), name ='nuevo_proovedor'),
    path("proveedor/editar/<int:pk>", ProovedorUpdateView.as_view(), name="editar_proovedor"),
    path("proveedor/delete/<int:id>",inavilitarProovedor, name="delete_proovedor"),
    #URL PARA LA SECCCION DE PRODUCTO
    path("producto/", ProductoViewList.as_view(), name="lista_producto"),
    path("producto/new", ProductoCreateView.as_view(), name="nuevo_producto"),
    path("producto/editar/<int:pk>", ProductoUpdateView.as_view(), name="editar_producto"),
    ##URL PARA LAS SECCION DE LOS PRODUCTOS EN BODEGA

    path("producto-bodega/", ProductoBodegaViewList.as_view(), name="lista_producto_bodega"),
    #URL PARA LA SECCCION DE PRODUCTO
    path("cuenta-trabajo/",CuentaListView.as_view(),name = "lista_cuenta"),
    path("cuenta-trabajo/nuevo",CuentaCreateView.as_view(),name = "nueva_cuenta"),
    path("cuenta-trabajo/editar/<int:pk>", CuentaUpdateView.as_view(),name = "editar_cuenta"),

    path("actividad/", ActividadListView.as_view(), name="lista_actividad"),
    path("actividad/nuevo", ActividadCreateView.as_view(), name="nuevo_actividad"),
    path("actividad/editar/<int:pk>", ActividadUpdateView.as_view(), name="editar_actividad"),

     path("asistencia/", AsistenciaListView.as_view(), name="lista_asistencia"),
]