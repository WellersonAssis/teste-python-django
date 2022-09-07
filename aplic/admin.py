from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Curso


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carga_horaria')