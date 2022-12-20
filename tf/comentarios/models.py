from django.db import models
from noticias.models import Noticias
from usuarios.models import Usuario
import datetime
# Create your models here.
class Comentarios(models.Model):
    fecha = models.DateTimeField(default=datetime.datetime.now) 
    comentario=models.TextField()

    #1 a muchos
    usuario = models.ForeignKey(Usuario,on_delete=models.SET_NULL,null=True,related_name="usuario",blank=True)
    noticia = models.ForeignKey(Noticias,on_delete=models.SET_NULL,null=True,related_name="noticias",blank=True)

    def __str__(self):
        return self.comentario