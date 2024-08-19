from django import forms

class LoginForms(forms.Form):
    nombre_login=forms.CharField(
        label = "Nombre de Login",
        required=True,
        max_length=100,
         widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Ej: Maravilla Toscano'
            }
            #atributos
        )

    )
    
    contraseña=forms.CharField(
        label = "Contraseña",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Escriba su contraseña'
            }
           
        )

    )