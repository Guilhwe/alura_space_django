from django.urls import path
from galeria.views import index, imagen

urlpatterns = [
    path('', index, name='index'),
    path('imagen/', imagen, name='imagen')
]