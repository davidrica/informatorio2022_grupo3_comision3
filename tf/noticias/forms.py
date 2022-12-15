
from django import forms

from .models import Noticias
from usuarios.models import Usuario

class NoticiasForm(forms.ModelForm):
    #fecha = forms.DateField(label="Fecha", widget=forms.DateTimeInput(attrs={"class": "form-control "}))
    titulo= forms.CharField(label="Titulo", widget=forms.TextInput(attrs={"class": "form-control"}))
    bajada= forms.CharField(label="Bajada", widget=forms.TextInput(attrs={"class": "form-control"}))
    cuerpo= forms.CharField(label="Cuerpo", widget=forms.TextInput(attrs={"class": "form-control"}))
    #usuario
    class Meta:
        model=Noticias
        fields=["fecha", "titulo", "bajada", "cuerpo", "usuario"]

class NoticiasFormLeer(forms.ModelForm):
    fecha = forms.DateField(label="Fecha", widget=forms.DateTimeInput(attrs={"class": "form-control "}))
    titulo= forms.CharField(label="Titulo", widget=forms.TextInput(attrs={"class": "form-control"}))
    bajada= forms.CharField(label="Bajada", widget=forms.TextInput(attrs={"class": "form-control"}))
    cuerpo= forms.CharField(label="Cuerpo", widget=forms.TextInput(attrs={"class": "form-control"}))
    #usuario
    class Meta:
        model=Noticias
        fields=["fecha", "titulo", "bajada", "cuerpo", "usuario"]


class NoticiasFormEditar(forms.ModelForm):
    usuario =forms.ModelChoiceField(queryset=Usuario.objects.all(), 
            label="Usuario", 
            widget=forms.Select( attrs={"class": "form-control"})
            )
    fecha = forms.DateTimeField(
            label="Fecha hora:", 
            widget= forms.DateTimeInput(attrs={ "class": "form-control"} )
            )
    titulo= forms.CharField(label="Titulo", widget=forms.TextInput(attrs={"class": "form-control"}))
    bajada= forms.CharField(label="Bajada", widget=forms.TextInput(attrs={"class": "form-control"}))
    cuerpo= forms.CharField(label="Cuerpo", widget=forms.TextInput(attrs={"class": "form-control"}))
    #usuario
    class Meta:
        model=Noticias
        fields=["usuario","fecha","titulo", "bajada", "cuerpo",]
