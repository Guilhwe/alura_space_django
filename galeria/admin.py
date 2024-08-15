from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display= ("id", "nombre", "leyenda")

admin.site.register(Fotografia, ListandoFotografias)

