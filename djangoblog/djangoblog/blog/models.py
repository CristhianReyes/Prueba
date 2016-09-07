from django.db import models
fomr django.utils import timezone

class Articulo(models.Model):
    autor = models.ForeingKey('auth.User')
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField (
        default = timezone.now)
    fecha_publicacion = models.DateTimeField (
        blank=True, null = true)

    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def_str_(self):
        return self.titulo
