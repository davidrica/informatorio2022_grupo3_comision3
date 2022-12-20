from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views


app_name="noticias"

urlpatterns = [
    path('admin/listado/', views.AdminListadoNoticias.as_view(), name="admin_listado_noticias"),
    # path('admin/nuevo/<int:pk>/', views.NuevoProducto.as_view(), name="admin_nuevo_producto"),
    path('admin/nuevo/', views.NuevaNoticia.as_view(), name="admin_nueva_noticia"),
    path('admin/editar/<int:pk>/', views.EditarNoticias.as_view(), name="editar"),
    path('admin/leer/<int:pk>/', views.LeerNoticias, name="leer"),
    #path('me-gusta/<int:id_producto>/', views.dar_me_gusta, name="dar_me_gusta")
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
