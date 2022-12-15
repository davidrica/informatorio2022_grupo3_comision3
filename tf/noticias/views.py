from django.shortcuts import render
from django.views.generic import ListView, UpdateView, FormView
from django.urls import reverse
from .models import Noticias
from .forms import NoticiasForm,NoticiasFormEditar

class AdminListadoNoticias(ListView):
    template_name = "noticias/listado.html"
    model = Noticias
    context_object_name = "noticias"
    paginate_by = 10

    def get_queryset(self):
        noticias = Noticias.objects.all()
        titulo = self.request.GET.get("buscador")
        if titulo:
            noticias = noticias.filter(titulo__contains=titulo)

        return noticias.order_by("titulo")




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

    
    # ===============================
    # query en django utilizando el orm
    

    contexto = {
        'noticias': Noticias.objects.filter(id=pk).first()
    }
    return render(request, template_name, contexto)