from django.shortcuts import render



def index(request):
    datos = {
    1:{"nombre": "Nebulosa de Carina",
       "Leyenda": "webbtelescope.org / NASA / James Webb"},
    2:{"nombre": "Galaxia NGC 1079",
       "leyenda": "nasa.org / NASA / Hubble"}
    }

    
    return render (request,'galeria/index.HTML',{"cards": datos})

def imagen(request):
    return render (request, 'galeria/imagen.HTML')