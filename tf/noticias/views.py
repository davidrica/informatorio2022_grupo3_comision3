from django.shortcuts import render
from django.views.generic import ListView, UpdateView, FormView,CreateView
from django.urls import reverse

from django.utils import timezone
from django.utils.dateparse import parse_date

import datetime
from django.contrib.auth.mixins import LoginRequiredMixin

from utils.mixins import IsAdminMixin

from comentarios.models import Comentarios
from .models import Noticias, Categorias 
from .forms import NoticiasForm,NoticiasFormEditar

class AdminListadoNoticias(ListView):
    template_name = "noticias/listado.html"
    model = Noticias
    context_object_name = "noticias"
    paginate_by = 1

    def get_queryset(self):
        my_date = datetime.datetime(2012, 2, 12)
        noticias = Noticias.objects.all()
        parametros = {}
        
        titulo   = self.request.GET.get("buscador")
        cat      = self.request.GET.get("categoria")
        fecha    = self.request.GET.get("fecha")
        if titulo:
            parametros["titulo__contains"]= titulo
#            parametros['titulo__contains']=
        if fecha:
            date = parse_date(fecha)
            
            parametros["fecha__gte"]= my_date.combine(date, datetime.time(0, 0)) 
            parametros["fecha__lte"]= my_date.combine(date, datetime.time(23, 59)) 
            
        if cat !='0' and cat is not None:
       
            parametros["categoria"]= cat

        
        noticias = noticias.filter(**parametros)
    
   
        
        return noticias.order_by("fecha")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
 
        context["listacategorias"] =  Categorias.objects.all()
        return context


class NuevaNoticia(CreateView):
    template_name = "noticias/nueva.html"
    model = Noticias
    form_class = NoticiasForm

    
    def get_success_url(self):
        return reverse("noticias:admin_listado_noticias")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["producto"] = Producto.objects.get(id=3) 
        return context
    def form_valid(self, form):
        f = form.save(commit=False)
        f.usuario_id = self.request.user.id
        return super(NuevaNoticia, self).form_valid(form)



class EditarNoticias(UpdateView):   
    model         = Noticias 
    template_name = "noticias/editar.html"
    form_class    = NoticiasFormEditar     

    def get_success_url(self):
        return reverse("noticias:admin_listado_noticias")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        return context


def LeerNoticias(request,pk):
    template_name = "noticias/leer.html"

    if request.method == "POST":
       
        c = Comentarios.objects.create(
            usuario=request.user, 
            comentario= request.POST["comentar"],
            noticia= Noticias.objects.get(id=pk), 

        )
    

    contexto = {
        'noticias': Noticias.objects.get(id=pk), 
        'comentarios':Comentarios.objects.filter(noticia=pk)
    }
    return render(request, template_name, contexto)