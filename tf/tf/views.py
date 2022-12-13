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