from django.shortcuts import render

from galeria.models import Fotografia

def index(request):
    fotografias = Fotografia.objects.all()

    
    return render (request,'galeria/index.HTML',{"cards": fotografias})

def imagen(request):
    return render (request, 'galeria/imagen.HTML')