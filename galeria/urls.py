from django.urls import path
from galeria.views import index, imagen

urlpatterns = [
    path('', index)
    path('imagen/', imagen)
]