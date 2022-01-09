from django.db import models


class Project(models.Model):

    title = models.CharField(max_length=100, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(upload_to='projects', verbose_name='Imagen')
    url_field = models.URLField(null=True, blank=True, verbose_name='Dirección Web')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'projecto'
        verbose_name_plural = 'projectos'
        ordering = ['-created']

    def __str__(self):
        return self.title
