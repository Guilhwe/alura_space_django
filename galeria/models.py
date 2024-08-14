from django.db import models

class Fotografia(models.Model):
    nombre = models.CharField(max_length=100, null= False, blank=False)
    #charfield para que el campo sea una string con el maximo de caracteres que quieres como nombre NULL false y blankfalse para aseguirar que haya algo escrito
    leyenda = models.CharField(max_length=150, null= False, blank=False)
    descripcion = models.TextField(null= False, blank=False)
    #Textfield porque es unn texto mas largo y elaborado, sin limite de caracteres pero asegurando cubrir el null y blank
    foto= models.CharField(max_length=100, null= False, blank=False)

    def __str__(self):
        return f"Fotografia [nombre={self.nombre}]"