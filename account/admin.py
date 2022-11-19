from django.contrib import admin
from .models import User, Unidad,Rol,Usuario,Tarea,TareaSub,TareaAce, Tarea2, Atraso, Problema, Jerarquia

# Register your models here.
admin.site.register(User)
admin.site.register(Unidad)
admin.site.register(Rol)
admin.site.register(Jerarquia)
admin.site.register(Usuario)
admin.site.register(Tarea)
admin.site.register(TareaSub)
admin.site.register(TareaAce)
admin.site.register(Tarea2)
admin.site.register(Atraso)
admin.site.register(Problema)