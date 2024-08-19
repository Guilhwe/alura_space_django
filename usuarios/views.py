from django.shortcuts import render
from usuarios.forms import LoginForms

def login(request):
    form=LoginForms()
    return render (request, 'usuarios/login.html', {"form" : form})

def registro(request):
    return render (request, 'usuarios/registro.html')
