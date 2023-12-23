from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    nombre = models.CharField(max_length= 30)
    titulo = models.CharField(max_length= 30)
    subtitulo = models.CharField(max_length= 30)
    cuerpo = models.TextField(max_length= 500)
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='post_images/', null=True, blank= True)
    lugar = models.CharField(max_length= 40)
    


    def __str__(self) -> str:
        return f"Nombre: {self.nombre} - Titulo: {self.titulo}"
    


    


    
