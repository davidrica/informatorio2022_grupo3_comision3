from django.shortcuts import render


def AgregarComentario(request):
    template_name = "noticias/leer.html"
    if request.method == "POST":
        username = request.POST["user"]
        print(username)
    # ===============================
    # query en django utilizando el orm
    

    contexto = {    }
    return render(request, template_name, contexto)


