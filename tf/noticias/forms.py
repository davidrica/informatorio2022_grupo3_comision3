
from django import forms
import datetime

from .models import Noticias, Categorias
from usuarios.models import Usuario

class NoticiasForm(forms.ModelForm):
    #fecha = forms.DateTimeField(
    #        label="Fecha hora:", 
    #        widget= forms.DateInput (attrs={"type": "datetime-local", "class": "form-control"} )
    #        )
    
    titulo= forms.CharField(label="Titulo", widget=forms.TextInput(attrs={"class": "form-control"}))
    bajada= forms.CharField(label="Bajada", widget=forms.TextInput(attrs={"class": "form-control"}))
    cuerpo= forms.CharField(label="Cuerpo", widget=forms.TextInput(attrs={"class": "form-control"}))
    categoria=forms.ModelChoiceField(queryset=Categorias.objects.all(),
            label="Cuerpo", 
            widget=forms.Select(attrs={"class": "form-control"}))
    #usuario
    class Meta:
        model=Noticias
        fields=["fecha", "titulo", "bajada", "cuerpo","categoria","imagen"]

class NoticiasFormLeer(forms.ModelForm):
   # fecha = forms.DateTimeField(
   #         label="Fecha hora:", 
   #         widget= forms.DateInput (attrs={"type": "datetime-local", "class": "form-control"} )
   #         )
    
    titulo= forms.CharField(label="Titulo", widget=forms.TextInput(attrs={"class": "form-control"}))
    bajada= forms.CharField(label="Bajada", widget=forms.TextInput(attrs={"class": "form-control"}))
    cuerpo= forms.CharField(label="Cuerpo", widget=forms.TextInput(attrs={"class": "form-control"}))
    categoria=forms.ModelChoiceField(queryset=Categorias.objects.all(),
            label="Cuerpo", 
            widget=forms.Select(attrs={"class": "form-control"}))
    #usuario
    class Meta:
        model=Noticias
        fields=["fecha", "titulo", "bajada", "cuerpo", "categoria","usuario","imagen"]


class NoticiasFormEditar(forms.ModelForm):
    
    #usuario =forms.ModelChoiceField(queryset=Usuario.objects.all(), 
     #       label="Usuario", 
    #        widget=forms.Select( attrs={"class": "form-control"})
    #        )
    #fecha = forms.DateTimeField(
    #        label="Fecha hora:", 
    #        widget= forms.DateTimeInput (attrs={"type": "datetime-local", "class": "form-control","value": "2022/12/22 09:41:00"} )
    #        )
    

    titulo= forms.CharField(label="Titulo", widget=forms.TextInput(attrs={"class": "form-control"}))
    bajada= forms.CharField(label="Bajada", widget=forms.TextInput(attrs={"class": "form-control"}))
    cuerpo= forms.CharField(label="Cuerpo", widget=forms.TextInput(attrs={"class": "form-control"}))
    categoria=forms.ModelChoiceField(queryset=Categorias.objects.all(),
            label="Cuerpo", 
            widget=forms.Select(attrs={"class": "form-control"}))
    #imagen = forms.FileField(
    #    label="Imagen",
    #    widget=forms.FileInput(
    #            attrs={"class": "form-control"}
    #            ) 
    #            )
            
    #usuario,
    class Meta:
        model=Noticias
        fields=["fecha","titulo", "bajada", "cuerpo","categoria","imagen"]
