from django.db import models

# Create your models here.

class Noticias(models.Model):
    fecha = models.DateTimeField()
    titulo=models.CharField(max_length=30)
    bajada=models.CharField(max_length=30)
    cuerpo=models.TextField()
