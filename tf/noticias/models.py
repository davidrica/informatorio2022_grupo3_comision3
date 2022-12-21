from django.db import models
from usuarios.models import Usuario
from categorias.models import Categorias

# Create your models here.

class Noticias(models.Model):
    fecha = models.DateTimeField()
    titulo=models.CharField(max_length=100, blank=True,null=True)
    bajada=models.CharField(max_length=100, blank=True) #subtítulo 
    cuerpo=models.TextField()
    imagen=models.ImageField(upload_to="noticias",null=True, blank=True)
    #1 a muchos
    usuario = models.ForeignKey(Usuario,on_delete=models.SET_NULL,null=True,related_name="usuarios",blank=True)
    categoria = models.ForeignKey(Categorias,on_delete=models.SET_NULL,null=True,related_name="categorias",blank=True)
    

    def __str__(self):
        return self.titulo