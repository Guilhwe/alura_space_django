from django.db import models
from datetime import datetime

class Fotografia(models.Model):

    opciones_de_categoria = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELLA", "Estrella"),
        ("GALAXIA", "Galaxia"),
        ("PLANETA", "Planeta")

    ]

    nombre = models.CharField(max_length=100, null= False, blank=False)
    #charfield para que el campo sea una string con el maximo de caracteres que quieres como nombre NULL false y blankfalse para aseguirar que haya algo escrito
    leyenda = models.CharField(max_length=150, null= False, blank=False)
    categoria = models.CharField(max_length =100, choices=opciones_de_categoria, default='')
    descripcion = models.TextField(null= False, blank=False)
    #Textfield porque es unn texto mas largo y elaborado, sin limite de caracteres pero asegurando cubrir el null y blank
    foto= models.ImageField(upload_to= "fotos/%Y/%m/%d", blank=True )
    publicada = models.BooleanField(default=False)
    fecha_fotografia = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.nombre