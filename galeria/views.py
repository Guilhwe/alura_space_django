from django.shortcuts import render


def index(request):
    return render (request,'galeria/index.HTML')
def imagen(request):
    return render (request, 'galeria/imagen.HTML')