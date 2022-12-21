from django import forms

from django.urls import reverse_lazy

from .models import Categorias

class CategoriasForm(forms.ModelForm):
    nombre = forms.CharField(label="nombre", widget=forms.TextInput(attrs={"class": "form-control"}))
    
    class Meta:
        model=Categorias
        fields=["nombre"]

class CategoriasFormEditar(forms.ModelForm):
    nombre = forms.CharField(label="nombre", widget=forms.TextInput(attrs={"class": "form-control"}))
    
    class Meta:
        model=Categorias
        fields=["nombre"]


