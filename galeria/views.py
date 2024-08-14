from django.shortcuts import render

datos = {
    1:{"nombre": "Nebulosa de Carina",
       "Leyenda": "webbtelescope.org / NASA / James Webb"},
    2:{"nombre": "Galaxia NGC 1079",
       "leyenda": "nasa.org / NASA / Hubble"}
}

def index(request):
    return render (request,'galeria/index.HTML')

def imagen(request):
    return render (request, 'galeria/imagen.HTML')