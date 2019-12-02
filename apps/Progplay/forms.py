from django import forms
from .models import Usuarios,Pais

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields =['NombreUsuario','Nickname','ClaveUsuario','Correo','idPais']
        labels ={
            'NombreUsuario': 'Nombre Completo',
            'Nickname': 'Nickname',
            'ClaveUsuario' : 'Contraseña',
            'Correo': 'Correo',
            'idPais': 'Pais'
        }
        widgets = {
            'NombreUsuario': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'placeholder': 'Ingrese Nombre',
                    'id':'NombreUsuario'
                }
            ),
             'Nickname': forms.TextInput(
                attrs= {
                    'class':'form-control',
                    'placeholder': 'Ingrese Nickname',
                    'id':'Nickname'
        }
             ),
            'ClaveUsuario': forms.PasswordInput(
                attrs= {
                    'class':'form-control',
                    'placeholder': 'Ingrese Contraseña',
                    'id':'ClaveUsuario'


        }

             ),

             'Correo': forms.EmailInput(
                attrs= {
                    'class':'form-control',
                    'placeholder': 'Ingrese Correo',
                    'id':'Correo'


        }

             ),

            'idPais': forms.Select(
                attrs= {
                    'class':'form-control',
                    'id':'idPais'


        }

             )
        }

            

