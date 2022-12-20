from django.shortcuts import render
from django.views.generic import ListView, UpdateView, FormView,CreateView,DeleteView
from django.urls import reverse
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from utils.mixins import IsAdminMixin


from .forms import CategoriasForm,CategoriasFormEditar

from .models import Categorias


# Create your views here.

class AdminListadoCategoria(LoginRequiredMixin, IsAdminMixin, ListView):
    template_name = "categorias/listado.html"
    model = Categorias
    context_object_name = "categorias"
    paginate_by = 5
    
    def get_queryset(self):
       
        categorias = Categorias.objects.all()
       
        nombre_categoria = self.request.GET.get("buscador")
        if nombre_categoria:
            categorias = categorias.filter(nombre__contains=nombre_categoria)
        return categorias.order_by("nombre")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
 
        #context["aaaa"] = "aaaaaaaaaaaaaa"
        return context


class NuevaCategoria(CreateView):
    template_name = "categorias/nueva.html"
    model = Categorias
    form_class = CategoriasForm

    
    def get_success_url(self):
        return reverse("categorias:admin_listado_categoria")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["producto"] = Producto.objects.get(id=3) 
        return context



class EditarCategoria(UpdateView):   
    model         = Categorias 
    template_name = "categorias/editar.html"
    form_class    = CategoriasFormEditar     

    def get_success_url(self):
        return reverse("categorias:admin_listado_categoria")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        return context

class EliminarCategoria(DeleteView):
    model = Categorias
    template_name = 'categorias/eliminar.html'
    success_message = 'La Categoria Fue eliminada.'
    success_url = reverse_lazy('categorias:admin_listado_categoria')
    context_object_name = "categorias"



