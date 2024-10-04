from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE    # Eliminamos el objeto profile cuando se elimino el objeto user
    )
    date_of_birth = models.DateField(blank=True, null=True)    # Fecha de nacimiento del usuario
    photo = models.ImageField(                                 # Imagen del usuario
        upload_to='users/%Y/%m/%d/',
        blank=True    # Nos permite que el campo sea opcional
    )
    
    def __str__(self):
        return f'Profile of {self.user.username}'