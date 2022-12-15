from django.shortcuts import render
from django.urls import reverse

from noticias.models import Noticias 
def inicio(request):
    template_name = "index.html"
    noticias = Noticias.objects.all()
    # ===============================
    # query en django utilizando el orm
    

    contexto = {
        'noticias': noticias
    }

    return render(request, template_name, contexto)

def about(request):
    template_name = "about.html"
    
    contexto = {}

    return render(request, template_name, contexto)

def contacto(request):
    template_name = "contacto.html"
    
    contexto = {}

    return render(request, template_name, contexto)

def descargas(request):
    template_name = "descargas.html"
    
    contexto = {}

    return render(request, template_name, contexto)

def mision(request):
    template_name = "mision.html"
    
    contexto = {}

    return render(request, template_name, contexto)

def vision(request):
    template_name = "vision.html"
    
    contexto = {}

    return render(request, template_name, contexto)

"""
sin uso
def login(request):
    print("aaaaaaaaaaa")
    contexto = {
        'noticias': 'aaaaaaaaaa'
    }
    #if request.method == "POST":
    ##    username = request.POST["user"]
    #    password = request.POST["password"]
    #    user = authenticate(request, username=username, password=password)
    #    if user is not None:

    #        login(request, user)

            #return redirect("/")

    #    else:

    #        form = AuthenticationForm(request.POST)

           #return render(request, "signin.html", {"form": form})
    
    return render(request, "login2.html", contexto)
"""