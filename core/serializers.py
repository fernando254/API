
from rest_framework import serializers
from .models import Usuario, Persona


class UsuarioSerializers(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = ['id','rut', 'nombre', 'apellido', 'correo']

class PersonaSerializers(serializers.ModelSerializer):

    class Meta:
        model = Persona
        fields = '__all__'