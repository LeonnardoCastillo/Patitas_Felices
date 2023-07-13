from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from .models import Stock
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = [ 'code','nombre', 'precio', 'imagen', 'cantidad', 'categoria' ]
        labels = {
            'code':'Codigo',
            'nombre':'Nombre',
            'precio':'Precio',
            'imagen':'Imagen',
            'cantidad':'Cantidad',
            'categoria':'Categoria'
            }
        widgets = {
            'code': forms.NumberInput(
            attrs={
                'placeholder':'Ingrese Codigo..',
                'id':'code',
                'class':'form-control',
                }
            ),
            'nombre': forms.TextInput(
            attrs={
                'placeholder':'Ingrese Nombre..',
                'id':'nombre',
                'class':'form-control',
                }
            ),
            'precio': forms.NumberInput(
            attrs={
                'placeholder':'Ingrese Precio..',
                'id':'precio',
                'class':'form-control',
                }
            ),
            'imagen': forms.FileInput(
            attrs={
                'class':'form-control',
                'id':'imagen',
                }
            ),
            'cantidad': forms.NumberInput(
            attrs={
                'placeholder':'Ingrese Cantidad..',
                'id':'cantidad',
                'class':'form-control',
                }
            ),
            'categoria': forms.Select(
            attrs={
                'placeholder':'Ingrese Categoria..',
                'id':'categoria',
                'class':'form-control',
                }
            )
        }