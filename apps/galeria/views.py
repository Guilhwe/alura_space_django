from django.shortcuts import render, get_object_or_404,redirect

from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms

from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'No estas logeado ')
        return redirect('login')


    fotografias = Fotografia.objects.order_by("fecha_fotografia").filter(publicada=True)
    return render (request,'galeria/index.HTML',{"cards": fotografias})

def imagen(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render (request, 'galeria/imagen.HTML',{"fotografia":fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'No estas logeado ')
        return redirect('login')
    fotografias = Fotografia.objects.order_by("fecha_fotografia").filter(publicada=True)
    if"buscar" in request.GET:
        nombre_a_buscar=request.GET['buscar']
        #este buscar hace referencia al imput name de manu en partials
        if nombre_a_buscar:
            fotografias=fotografias.filter(nombre__icontains=nombre_a_buscar)
            #este linea de codigo redefine la variable  fotografias y filtra las fotos para que solo enseñe las que contengan el termino elegido en nombre a buscar

    return render (request, "galeria/index.html", {"cards": fotografias})

def nueva_imagen(request):
    if not request.user.is_authenticated:
        messages.error(request, 'No estas logeado ')
        return redirect('login')
    form = FotografiaForms
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nueva imagen agregada')
            return redirect('index')
        
    return render (request, 'galeria/nueva_imagen.html',{'form' : form})

def editar_imagen(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)

    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fotografia editada con éxito')
            return redirect('index')

    return render(request, 'galeria/editar_imagen.html',{'form' : form, 'foto_id': foto_id})
    

def borrar_imagen(request, foto_id):
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Foto eliminada')
    return redirect('index')

def filtro(request, categoria):
    fotografias = Fotografia.objects.order_by("fecha_fotografia").filter(publicada=True, categoria=categoria)
    return render(request,'galeria/index.html',{"cards": fotografias})

#por cada ruta creamos un views definiendolo y recibiendo el request renderizandolo retornandolo y una ruta html