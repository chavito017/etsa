from django.urls import path
from principal.views import *

urlpatterns = [
    
    path('parametros/',Parametros, name='leerpar'),
#--------------------------------------------------URL Categoriataller ------------------------------------------------------------------------#
    
path('Categoriataller/', ListadoCategoriataller.as_view(template_name = "crud/Categoriataller/tables.html"), name='leerre'),

# La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
path('Categoriataller/detalle/<int:pk>',CategoriatallerDetalle.as_view(template_name = "crud/Categoriataller/detalle.html"), name='detallesre'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
path('Categoriataller/editar/<int:pk>', CategoriatallerActualizar.as_view(template_name = "crud/Categoriataller/actualizar.html"), name='actualizarre'), 

# La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
path('Categoriataller/eliminar/<int:pk>', CategoriatallerEliminar.as_view(), name='crud/Categoriataller/eliminar.html'),     
 #---------------------------------------------------URL Categoriataller ------------------------------------------------------------------------#
 

# path('parametros/',Parametros, name='leerpar'),
# #--------------------------------------------URL Servicio ------------------------------------------------------------------------#
    
# path('Servicio/', ListadoServicio.as_view(template_name = "crud/Servicio/tables.html"), name='leerre'),

# # La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
# path('Servicio/detalle/<int:pk>', ServiciolDetalle.as_view(template_name = "crud/Servicio/detalle.html"), name='detallesre'),

# # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
# path('Servicio/editar/<int:pk>', ServicioActualizar.as_view(template_name = "crud/Servicio/actualizar.html"), name='actualizarre'), 

# # La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
# path('Servicio/eliminar/<int:pk>', ServicioEliminar.as_view(), name='crud/Servicio/eliminar.html'),     
#--------------------------------------------URL Servicio ------------------------------------------------------------------------#
#--------------------------------------------URL Usuario ------------------------------------------------------------------------#

  path('parametros/',Parametros, name='leerpar'),
#--------------------------------------------------URL Categoriataller ------------------------------------------------------------------------#
    
path('Usuario/', ListadoUsuario.as_view(template_name = "crud/Usuario/tables.html"), name='leerru'),

# La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
path('Usuario/detalle/<int:pk>',UsuarioDetalle.as_view(template_name = "crud/Usuario/detalle.html"), name='detallesru'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
path('Usuario/editar/<int:pk>', UsuarioActualizar.as_view(template_name = "crud/Usuario/actualizar.html"), name='actualizarru'), 

# La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
path('Usuario/eliminar/<int:pk>', UsuarioEliminar.as_view(), name='crud/Usuario/eliminar.html'),     
 #---------------------------------------------------URL Categoriataller ------------------------------------------------------------------------#


]