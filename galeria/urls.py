from django.urls import path
from galeria.views import index, imagen

urlpatterns = [
    path('', index, name='index'),
    path('imagen/<int:foto_id>', imagen, name='imagen')
]