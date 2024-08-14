from django.shortcuts import render, get_object_or_404

from galeria.models import Fotografia

def index(request):
    fotografias = Fotografia.objects.all()

    
    return render (request,'galeria/index.HTML',{"cards": fotografias})

def imagen(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render (request, 'galeria/imagen.HTML',{"fotografia":fotografia})