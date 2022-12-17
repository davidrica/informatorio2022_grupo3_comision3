from django.db import models
from noticias.models import Noticias
from usuarios.models import Usuario

# Create your models here.
class Comentarios(models.Model):
    fecha = models.DateTimeField() 
    comentario=models.TextField()

    #1 a muchos
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,null=True,related_name="usuario",blank=True)
    noticia = models.ForeignKey(Noticias,on_delete=models.CASCADE,null=True,related_name="noticias",blank=True)