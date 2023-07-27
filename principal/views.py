from django.shortcuts import render
from principal.models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.contrib import messages 

# Create your views here.
def Home(request):
    
    return render (request, "index.html")

def Parametros (request):
    return render (request, "crud/index.html")  

def Login(request):
    return render (request, "login.html")

#--------------------------------------------------Categoriataller-----------------------------------------------------#
class ListadoCategoriataller(CreateView,ListView,SuccessMessageMixin):

    model = Categoriataller
    form = Categoriataller
    fields = "__all__"
    
    success_message ='Categoriataller creado correctamente'
    def get_success_url(self):        
        return reverse('principal:leerre') # Redireccionamos a la vista principal 'leer' 
    
class CategoriatallerDetalle (DetailView):
    model =Categoriataller

class CategoriatallerActualizar(SuccessMessageMixin,UpdateView):
    model =Categoriataller
    form = Categoriataller
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Cateserv' de nuestra Base de Datos 
    success_message = 'Categoriataller Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('principal:leer') # Redireccionamos a la vista principal 'leer'
    
class CategoriatallerEliminar(SuccessMessageMixin, DeleteView): 
    model = Categoriataller
    form = Categoriataller
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoriataller Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerre') # Redireccionamos a la vista principal 'leer'
    
 #----------------------------------------------fin Categoriataller-----------------------------------------------------#

# #--------------------------------------------------------Empresa-----------------------------------------------------#
class ListadoEmpresa(CreateView,ListView,SuccessMessageMixin):

    model = Empresa
    form = Empresa
    fields = "__all__"
    
    success_message ='Empresa creado correctamente'
    def get_success_url(self):        
        return reverse('principal:leerem') # Redireccionamos a la vista principal 'leer' 
    
class EmpresalDetalle (DetailView):
    model =Empresa

class EmpresaActualizar(SuccessMessageMixin,UpdateView):
    model =Empresa
    form = Empresa
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'regional' de nuestra Base de Datos 
    success_message = 'Empresa Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('principal:leerem') # Redireccionamos a la vista principal 'leer'
    
class EmpresaEliminar(SuccessMessageMixin, DeleteView): 
    model = Empresa
    form = Empresa
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Empresa Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerem') # Redireccionamos a la vista principal 'leer'
    

#------------------------------------------------------usuario-----------------------------------------------------#
class ListadoUsuario(CreateView,ListView,SuccessMessageMixin):

    model = Usuario
    form = Usuario
    fields = "__all__"
    
    success_message ='Usuario creado correctamente'
    def get_success_url(self):        
        return reverse('principal:leerre') # Redireccionamos a la vista principal 'leer' 
    
class UsuarioDetalle (DetailView):
    model =Usuario

class UsuarioActualizar(SuccessMessageMixin,UpdateView):
    model =Usuario
    form = Usuario
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'regional' de nuestra Base de Datos 
    success_message = 'Usuario Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('principal:leer') # Redireccionamos a la vista principal 'leer'
    
class UsuarioEliminar(SuccessMessageMixin, DeleteView): 
    model = Usuario
    form = Usuario
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Usuario Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('principal:leerre') # Redireccionamos a la vista principal 'leer'
    
#----------------------------------------------------------Usuario-----------------------------------------------------#
#--------------------------------------------------------Departamento-----------------------------------------------------#
class ListadoDepartamento(CreateView,ListView,SuccessMessageMixin):

    model = Departamento
    form = Departamento
    fields = "__all__"
    
    success_message ='Departamento creado correctamente'
    def get_success_url(self):        
        return reverse('principal:leerde') # Redireccionamos a la vista principal 'leer' 
    
class DepartamentoDetalle (DetailView):
    model =Categoriataller

class DepartamentoActualizar(SuccessMessageMixin,UpdateView):
    model =Departamento
    form = Departamento
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Cateserv' de nuestra Base de Datos 
    success_message = 'Departamento Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('principal:leerdep') # Redireccionamos a la vista principal 'leer'
    
class DepartamentoEliminar(SuccessMessageMixin, DeleteView): 
    model = Departamento
    form = Departamento
 #------------------------------------------------------------------------------servisio-----------------------------------------------------#

 #------------------------------------------------------------------------------Municipio-----------------------------------------------------#
class ListadoMunicipio(CreateView,ListView,SuccessMessageMixin):

    model = Municipio
    form = Municipio
    fields = "__all__"
    
    success_message ='Municipio creado correctamente'
    def get_success_url(self):        
        return reverse('principal:leermun') # Redireccionamos a la vista principal 'leer' 
    
class MunicipioDetalle (DetailView):
    model =Municipio

class MunicipioActualizar(SuccessMessageMixin,UpdateView):
    model =Municipio
    form = Municipio
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Cateserv' de nuestra Base de Datos 
    success_message = 'Municipio Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('principal:leer') # Redireccionamos a la vista principal 'leer'
    
class MunicipioEliminar(SuccessMessageMixin, DeleteView): 
    model = Municipio
    form = Municipio
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Municipio Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('principal:leermun') # Redireccionamos a la vista principal 'leer'
    
#     #-----------------------------------------------------------servisio-----------------------------------------------------#


#---------------------------------------------------------------CategoriaServicio-----------------------------------------------------#
class ListadoCategoriaservicio(CreateView,ListView,SuccessMessageMixin):

    model = Categoriaservicio
    form = Categoriaservicio
    fields = "__all__"
    
    success_message ='Categoriaservicio creado correctamente'
    def get_success_url(self):        
        return reverse('principal:leercat') # Redireccionamos a la vista principal 'leer' 
    
class CategoriaservicioDetalle (DetailView):
    model =Categoriaservicio

class CategoriaservicioActualizar(SuccessMessageMixin,UpdateView):
    model =Categoriaservicio
    form = Categoriaservicio
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'municipio' de nuestra Base de Datos 
    success_message = 'Categoriaservicio Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('principal:leercat') # Redireccionamos a la vista principal 'leer'
    
class CategoriaservicioEliminar(SuccessMessageMixin, DeleteView): 
    model = Categoriaservicio
    form = Categoriaservicio
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Categoriaservicio Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('principal:leercat') # Redireccionamos a la vista principal 'leer'
    
#     #-----------------------------------------------------------servisio-----------------------------------------------------#

#--------------------------------------------------Contrato-----------------------------------------------------#
class ListadoContrato(CreateView,ListView,SuccessMessageMixin):

    model = Contrato
    form = Contrato
    fields = "__all__"
    
    success_message ='Contrato creado correctamente'
    def get_success_url(self):        
        return reverse('principal:leercon') # Redireccionamos a la vista principal 'leer' 
    
class ContratoDetalle (DetailView):
    model =Contrato

class ContratoActualizar(SuccessMessageMixin,UpdateView):
    model =Contrato
    form = Contrato
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'Cateserv' de nuestra Base de Datos 
    success_message = 'Contrato Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 

    def get_success_url(self):               
        return reverse('principal:leercon') # Redireccionamos a la vista principal 'leer'
    
class ContratoEliminar(SuccessMessageMixin, DeleteView): 
    model = Contrato
    form = Contrato
    fields = "__all__"     
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Contrato Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('principal:leercon') # Redireccionamos a la vista principal 'leer'
    
 #----------------------------------------------fin Contrato-----------------------------------------------------#
