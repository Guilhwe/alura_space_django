from django.contrib import admin
from galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display= ("id", "nombre", "leyenda")
    list_display_links = ("id", "nombre")
    search_fields = ("nombre",)
    list_filter = ("categoria",)
    list_per_page = 10

admin.site.register(Fotografia, ListandoFotografias)

