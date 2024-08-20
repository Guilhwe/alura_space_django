from django.shortcuts import render
from usuarios.forms import LoginForms, RegistroForms

def login(request):
    form=LoginForms()
    return render (request, 'usuarios/login.html', {"form" : form})

def registro(request):
    form = RegistroForms()
    return render (request, 'usuarios/registro.html', {"form" : form})
