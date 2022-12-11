from django.shortcuts import render
from django.contrib.auth import authenticate, login

from noticias.models import Noticias 
def inicio(request):
    template_name = "index.html"
    
    # ===============================
    # query en django utilizando el orm
    """
    p = Producto.objects.create(
        nombre="Pantalon",
        precio=2000,
        descripcion="Pantalon azul"
    )
    """

    contexto = {
        'noticias':  Noticias.objects.all()
    }

    return render(request, template_name, contexto)


def login(request):
   
    contexto = {
        'noticias': 'aaaaaaaaaa'
    }
    #if request.method == 'GET':
    ##    username = request.GET['username']
    ##    password = request.GET['password']
    #    user = authenticate(username="david", password="david")
    #    contexto = {}
       
    return render(request, "login.html", contexto)    