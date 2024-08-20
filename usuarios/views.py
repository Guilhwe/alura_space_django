from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, RegistroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login(request):
    form=LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            nombre=form['nombre_login'].value()
            
            contraseña= form['contraseña'].value()
        usuario= auth.authenticate(
            request,
            username=nombre,
            password= contraseña
            
            )
        if usuario is not None:
            auth.login(request,usuario)
            messages.success(request,'f{nombre} logeado con succeso')
            return redirect('index')
        else:
            messages.error(request,'ERROR de login')
            return redirect('login')



    return render (request, 'usuarios/login.html', {"form" : form})


def registro(request):
    form = RegistroForms()

    if request.method == 'POST':
        form =RegistroForms(request.POST)

        
        if form.is_valid():
             #para verificar si el formulario es valido
             if form['contraseña1'].value () != form['contraseña2'].value():
                messages.error(request,'Las contraseñas no coinciden')
                return redirect('registro')
             #verficar si las contraseñas son iguales
             
        nombre = form['nombre_registro'].value()
        email = form['email'].value()
        contraseña = form['contraseña1'].value()
        #guardar las informaciones del formularia en otras variables para hacerlo  mas manejable
        
        if User.objects.filter(username=nombre).exists():
             messages.error(request, 'El usuario ya está registrado')
             return redirect('registro')
        #verifica si el usuario ya exite
        usuario = User.objects.create_user(
                username = nombre,
                email=email,
                password=contraseña,
                )
        usuario.save()
        messages.success(request, 'Registrado con éxito')
        #crea nuevo usuario
        return redirect('login')
    #redirecciona a login


    return render (request, 'usuarios/registro.html', {"form" : form})
