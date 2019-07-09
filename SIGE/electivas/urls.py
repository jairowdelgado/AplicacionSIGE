from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [     
     # La ruta 'leer' en donde listamos todos los registros o postres de la Base de Datos
    path('', views.ElectivaListado.as_view(template_name = "index.html"), name='leer'),
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles de un postre o registro 
    path('detalle/<int:pk>', views.ElectivaDetalle.as_view(template_name = "detalles.html"), name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo postre o registro  
    path('crear', views.ElectivaCrear.as_view(template_name = "crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un postre o registro de la Base de Datos 
    path('editar/<int:pk>', views.ElectivaActualizar.as_view(template_name = "actualizar.html"), name='actualizar'), 
 
    # La ruta 'eliminar' que usaremos para eliminar un postre o registro de la Base de Datos 
    path('eliminar/<int:pk>', views.ElectivaEliminar.as_view(), name='eliminar'),  
]
