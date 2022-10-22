from django.contrib import admin

from .models import Comuna, Usuario, Persona

# Register your models here.

admin.site.register(Comuna)
admin.site.register(Persona)
admin.site.register(Usuario)
