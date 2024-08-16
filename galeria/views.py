from django.shortcuts import render, get_object_or_404

from galeria.models import Fotografia

def index(request):
    fotografias = Fotografia.objects.order_by("fecha_fotografia").filter(publicada=True)


    
    return render (request,'galeria/index.HTML',{"cards": fotografias})

def imagen(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render (request, 'galeria/imagen.HTML',{"fotografia":fotografia})

def buscar(request):
    return render (request, "buscar.html")
#por cada ruta creamos un views definiendolo y recibiendo el request renderizandolo retornandolo y una ruta html