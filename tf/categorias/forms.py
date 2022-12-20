from django import forms

from django.urls import reverse_lazy
from bootstrap_modal_forms.forms import BSModalModelForm, BSModalForm
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



class BookModelForm(BSModalModelForm):
    publication_date = forms.DateField(
        error_messages={'invalid': 'Enter a valid date in YYYY-MM-DD format.'}
    )

    class Meta:
        model = Categorias
        exclude = ['timestamp']
