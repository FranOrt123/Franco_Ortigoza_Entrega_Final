from django.db import models

class Camiseta(models.Model):
    talle = models.CharField(max_length=5)
    modelo =models.CharField(max_length=100)
    club = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="imagenes_camisetas", null=True, blank=True)

def __str__(self):
    return f"Camiseta({self.id})-{self.club} -{self.modelo}-{self.talle}"