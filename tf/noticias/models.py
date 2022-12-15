from django.db import models
from usuarios.models import Usuario

# Create your models here.

class Noticias(models.Model):
    fecha = models.DateTimeField()
    titulo=models.CharField(max_length=30)
    bajada=models.CharField(max_length=30) #subtítulo 
    cuerpo=models.TextField()
    #1 a muchos
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,null=True,related_name="usuarios",blank=True)

    def __str__(self):
        return self.titulo