
from django.shortcuts import render

from rest_framework import viewsets
from .models import Persona, Usuario 
from .serializers import PersonaSerializers, UsuarioSerializers

from django.db import connection #importar conecion de oracle

import cx_Oracle #importacion de oracle

# Create your views here.


def home(request):
    
    data = {

        'personas': listado_personas(),
        'comunas': listado_comunas(),
    }

    if request.method == 'POST':
        rut = request.POST.get('rut')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        fecha_nacimiento = request.POST.get('fecha')
        direccion = request.POST.get('direccion')
        comuna_id = request.POST.get('comuna')

        salida = agregar_persona(rut, nombre, apellido, fecha_nacimiento, direccion, comuna_id)
        if salida ==1:
            data['mensaje'] = 'agregado correctamente'
            data['personas'] = listado_personas()
        else:
            data['mensaje'] = 'no se ha podido guardar'

    return render(request, "core/home.html", data)


def listado_personas():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor() # parametro de salida

    cursor.callproc("SP_LISTAR_PERSONAS", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def listado_comunas():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor() # parametro de salida

    cursor.callproc("SP_LISTAR_COMUNAS", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista

def agregar_persona(rut, nombre, apellido, fecha_nacimiento, direccion, comuna_id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_PERSONA', [rut, nombre, apellido, fecha_nacimiento, direccion, comuna_id, salida])
    return salida.getvalue()





class UsuariViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializers


class PersonaVievSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializers

