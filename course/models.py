from django.db import models
import uuid 
from django.contrib import admin 

# Create your models here.
class areasCurso(models.Model):
    id_area_curso  = models.UUIDField(primary_key=True, default=uuid.uuid4)
    nombre_area_curso = models.CharField(max_length=100)
    descripcion_area_curso = models.TextField(max_length=600)
    id_curso = models.IntegerField()
    nombre_icono = models.CharField(max_length=100)
    #id_curso  = models.ForeignKey('id_curso', on_delete=models.SET_NULL, null=True)
    class Meta:
        db_table='areas_de_curso'
        ordering=['id_curso']

    
class mostrar(admin.ModelAdmin):
    list_display = ('nombre_area_curso','descripcion_area_curso')


admin.site.register(areasCurso,mostrar)
