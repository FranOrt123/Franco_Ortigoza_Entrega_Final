from django import forms

class CrearCamisetas(forms.Form):
    club = forms.CharField(max_length=50)
    modelo = forms.CharField(max_length=100)
    talle = forms.CharField(max_length=5)
    imagen = forms.ImageField(required=False)

class BuscarCamisetas(forms.Form):
    club = forms.CharField(max_length=50, required=False)
    