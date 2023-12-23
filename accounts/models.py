from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class User_profile(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='profile_images/', null=True, blank= True)
    nombre = models.CharField(max_length= 40)
    descripcion = models.CharField(max_length=250)
    link = models.URLField(blank=True, null=True)
    correo = models.EmailField()
    contraseña = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username









@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        User_profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.user.save()