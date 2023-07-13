from django.urls import path
from patitas.views import *

urlpatterns=[
    path('', Inicio, name="Inicio"),
    path('organizacion/', organizacion, name="organizacion"),
    path('Productos/', Productos, name="Productos"),
    path('Formulario/', Formulario, name="Formulario"),
    path('Api/', Api, name="Api"),
    path('Ver/', Ver, name="Ver"),
    path('crear/', crear, name="crear"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('modificar/<id>', modificar, name="modificar"),
    path('registrar/', registrar, name="registrar"),

    path('tienda/',tienda, name="tienda"),
    path('tienda/',tienda, name="tienda"),
    path('generarBoleta/', generarBoleta, name="generarBoleta"),
    path('agregar/<id>', agregar_producto, name="agregar"),
    path('eliminar/<id>', eliminar_producto, name="eliminar"),
    path('restar/<id>', restar_producto, name="restar"),
    path('limpiar/', limpiar_carrito, name="limpiar"),
]