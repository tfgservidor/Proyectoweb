from django.db import models
from embed_video.fields import EmbedVideoField


# Create your models here.



class Recomendacion(models.Model):
    titulo=models.CharField(max_length=200)
    video=EmbedVideoField(null=True, blank=True)
    princ=models.ForeignKey('Principal', on_delete=models.CASCADE,null=True, blank=True)
    #categorias=models.ManyToManyField(Categoria)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='recomendacion'
        verbose_name_plural='recomendaciones'
    
    def __str__(self):
        return self.titulo

class Principal(models.Model):
    nombre=models.CharField(max_length=50)
    #recomendacion=models.ManyToManyField(Recomendacion)
    categ=models.ForeignKey('Categoria', on_delete=models.CASCADE,null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='principal'
        verbose_name_plural='principales'
    
    def __str__(self):
        return self.nombre 

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    #principal=models.ManyToManyField(Principal)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
    
    def __str__(self):
        return self.nombre


