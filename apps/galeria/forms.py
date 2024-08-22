from django import forms

from apps.galeria.models import Fotografia

class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude =['publicada',]
        labels ={
            'descripcion': 'Descripción',
            'fecha_fotografia' : 'Fecha de registro',
            'usuario': 'Usuario'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'leyenda': forms.TextInput(attrs={'class': 'form-control'}),
            'categotria': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control'}),
            'fecha_fotografia': forms.DateInput(
                format= '%d/%m/%Y',
                attrs={
                    'type':'date',
                    'class': 'form-control'
                    }
                    ),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }