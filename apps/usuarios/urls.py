from django.urls import path
from apps.usuarios.views import login, registro, logout

urlpatterns =[
    path('login', login, name='login'),
    path('registro', registro, name='registro'),
    path('logout',logout, name='logout')

] 
   