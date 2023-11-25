from django.db import models
from django.contrib.auth.models import User

class Avatar( models.Model ):

    User = models.OneToOneField( User , on_delete=models.CASCADE)
    Imagen = models.ImageField( upload_to = 'Avatar/' )

    def save(self, *args, **kwargs):
        try:
            this = Avatar.objects.get(id=self.id)
            if this.Imagen != self.Imagen:
                this.Imagen.delete(save=False)
        except: pass # cuando se crea una nueva imagen, no existe aún
        super(Avatar, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.Imagen.delete(save=False)
        super(Avatar, self).delete(*args, **kwargs)

