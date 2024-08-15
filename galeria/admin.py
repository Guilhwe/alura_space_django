from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display= ("id", "nombre", "leyenda")
    list_display_links = ("id", "nombre")
    search_fields = ("nombre",)

admin.site.register(Fotografia, ListandoFotografias)

