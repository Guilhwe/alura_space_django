from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, RegistroForms
from django.contrib.auth.models import User

def login(request):
    form=LoginForms()
    return render (request, 'usuarios/login.html', {"form" : form})

def registro(request):
    form = RegistroForms()

    if request.method == 'POST':
        form =RegistroForms(request.POST)

        if form.is_valid():
             if form['contraseña1'].value () != form['contraseña2'].value():
                return redirect('registro')
             
        nombre = form['nombre_registro'].value()
        email = form['email'].value()
        contraseña = form['contraseña1'].value()
        
        if User.objects.filter(username=nombre).exists():
             return redirect('registro')
        usuario = User.objects.create_user(
                username = nombre,
                email=email,
                password=contraseña,
                )
        usuario.save()
        return redirect('login')

    return render (request, 'usuarios/registro.html', {"form" : form})
