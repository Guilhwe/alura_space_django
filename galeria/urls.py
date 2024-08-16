from django.urls import path
from galeria.views import index, imagen, buscar

urlpatterns = [
    path('', index, name='index'),
    path('imagen/<int:foto_id>', imagen, name='imagen'),
    path("buscar", buscar, name="buscar"),
    #para crear la ruta nueva se utiliza la formula de arriba: path que apunta a la ruta de views que se crea en views y se le asigna un nombre( no olvidar importar la ruta)
]