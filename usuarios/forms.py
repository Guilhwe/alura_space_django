from django import forms

class LoginForms(forms.Form):
    nombre_login=forms.CharField(
        label = "Nombre de Login",
        required=True,
        max_length=100

    )
    
    contraseña=forms.CharField(
        label = "Contraseña",
        required=True,
        max_length=70,
        widget=forms.PasswordInput()

    )