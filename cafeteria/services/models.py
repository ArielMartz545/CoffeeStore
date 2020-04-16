from django.db import models

# Create your models here.

class Services(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    subtitle = models.CharField(max_length=200, verbose_name="Subtitulos")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="imagen", upload_to="services")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de edicion")

    class Meta:
        #nombres que apareceran en la bd
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
       #para ordenar de manera decendiente
        ordering = ['-created']

    def _str_(self):
        return self.title