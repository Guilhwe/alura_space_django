from django.urls import path
from apps.galeria.views import index, imagen, buscar, nueva_imagen, editar_imagen, borrar_imagen 

urlpatterns = [
    path('', index, name='index'),
    path('imagen/<int:foto_id>', imagen, name='imagen'),
    path("buscar", buscar, name="buscar"),
    path('nueva-imagen', nueva_imagen, name='nueva_imagen'),
    path('editar-imagen', editar_imagen, name='editar_imagen'),
    path('borrar-imagen', borrar_imagen, name='borrar_imagen'),
    #para crear la ruta nueva se utiliza la formula de arriba: path que apunta a la ruta de views que se crea en views y se le asigna un nombre( no olvidar importar la ruta)
]