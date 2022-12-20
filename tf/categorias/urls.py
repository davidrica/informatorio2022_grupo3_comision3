from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name="categorias"

urlpatterns = [
    path('admin/listado/', views.AdminListadoCategoria.as_view(), name="admin_listado_categoria"),
    path('admin/nuevo/', views.NuevaCategoria.as_view(), name="admin_nueva_categoria"),
    path('admin/editar/<int:pk>/', views.EditarCategoria.as_view(), name="editar"),
    path('admin/eliminar/<int:pk>', views.EliminarCategoria.as_view(), name='eliminar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
