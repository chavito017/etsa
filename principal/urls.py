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
 


#--------------------------------------------URL Empresa ------------------------------------------------------------------------#
    
path('Empresa/', ListadoEmpresa.as_view(template_name = "crud/Empresa/tables.html"), name='leerem'),

# La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
path('Empresa/detalle/<int:pk>', EmpresalDetalle.as_view(template_name = "crud/Empresa/detalle.html"), name='detallesreser'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
path('Empresa/editar/<int:pk>', EmpresaActualizar.as_view(template_name = "crud/Empresa/actualizar.html"), name='actualizarreser'), 

# La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
path('Empresa/eliminar/<int:pk>', EmpresaEliminar.as_view(), name='crud/Empresa/eliminar.html'),     
# --------------------------------------------URL Empresa ------------------------------------------------------------------------#


#------------------------------------------------------URL Categoriataller ------------------------------------------------------------------------#
    
path('Usuario/', ListadoUsuario.as_view(template_name = "crud/Usuario/tables.html"), name='leerru'),

# La ruta 'detalles' en donde mostraremos una pagina con los detalles de un Categoria o registro 
path('Usuario/detalle/<int:pk>',UsuarioDetalle.as_view(template_name = "crud/Usuario/detalle.html"), name='detallesru'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
path('Usuario/editar/<int:pk>', UsuarioActualizar.as_view(template_name = "crud/Usuario/actualizar.html"), name='actualizarru'), 

# La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
path('Usuario/eliminar/<int:pk>', UsuarioEliminar.as_view(), name='crud/Usuario/eliminar.html'),     
 #---------------------------------------------------URL Categoriataller ------------------------------------------------------------------------#

path('usuarioC/', ListadoUsuario.as_view(template_name = "tienda/index_principal.html"), name='tienda'),
path('usuarioC/detaller<int:pk>', UsuarioDetalle.as_view(template_name = "tienda/index.html"), name='tienda'),


#------------------------------------------------------URL Departamento ------------------------------------------------------------------------#   
path('Departamento/', ListadoDepartamento.as_view(template_name = "crud/Departamento/tables.html"), name='leerde'),

# La ruta 'Departamento' en donde mostraremos una pagina con los detalles de un Categoria o registro 
path('Departamento/detalle/<int:pk>',DepartamentoDetalle.as_view(template_name = "crud/Departamento/detalle.html"), name='detallesdep'),

# La ruta 'actualizar' en donde mostraremos un formulario para actualizar un categoriao registro de la Base de Datos 
path('Departamento/editar/<int:pk>', DepartamentoActualizar.as_view(template_name = "crud/Departamento/actualizar.html"), name='actualizarde'), 

# La ruta 'eliminar' que usaremos para eliminar un Categoria o registro de la Base de Datos 
path('Departamento/eliminar/<int:pk>',DepartamentoEliminar.as_view(), name='crud/Departamento/eliminar.html'),     
 #---------------------------------------------------URL Departamento ------------------------------------------------------------------------#

]