from django.db import models
from usuarios.models import Usuario
from categorias.models import Categorias

# Create your models here.

class Noticias(models.Model):
    fecha = models.DateTimeField()
    titulo=models.CharField(max_length=30)
    bajada=models.CharField(max_length=30) #subtítulo 
    cuerpo=models.TextField()
    imagen=models.ImageField(upload_to="noticias",null=True, blank=True)
    #1 a muchos
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,null=True,related_name="usuarios",blank=True)
    categoria = models.ForeignKey(Categorias,on_delete=models.CASCADE,null=True,related_name="categorias",blank=True)
    def __str__(self):
        return self.titulo