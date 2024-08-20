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

class RegistroForms(forms.Form):
        
        #para heredar las caracteristicas del forms
        nombre_registro=forms.CharField(
        label = "Escribe tu usuario",
        required=True,
        max_length=100,
         widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Ej: Mara34'
            }
            
        )

    )
        email= forms.EmailField(
        label = "Escribe tu email",
        required=True,
        max_length=100,
         widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Ej: Maravilla@gmail.com'
            }
            
        )
    )
        contraseña1=forms.CharField(
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
        contraseña2=forms.CharField(
        label = "Contraseña",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Escriba su contraseña otra vez'
            }
           
        )

    )
        def clean_nombre_registro(self):
      #para añadir metodos de validacion
            nombre = self.cleaned_data.get('nombre_registro')
            if nombre:
                nombre = nombre.strip()
                if ' ' in nombre:
                    raise forms.ValidationError('No es posible insertar espacios en el usuario')
                else:
                    return nombre
    
    
