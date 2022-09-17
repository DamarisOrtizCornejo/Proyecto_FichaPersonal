from django.urls import path

from .views.empleados.views import EmpleadoListView, CrearEmpleado, ActualizarEmpleado, EliminarEmpleado
from .views.Departamento.views import DepartamentoListView, CrearDepartamento, ActualizarDepartamento, EliminarDepartamento
from .views.Cargo.views import CargoListView, CrearCargo, ActualizarCargo, EliminarCargo
from .views.ContactoEmergencia.views import ContactoEmergenciaListView, RegistroContactoEmergenciaListView, CrearContactoEmergencia, ActualizarContactoEmergencia, EliminarContactoEmergencia
from .views.InformacionAcademica.views import InfoAcademicaListView, RegistroInfoAcademicaListView, CrearInfoAcademica, ActualizarInfoAcademica, EliminarInfoAcademica
from .views.Capacitaciones.views import CapacitacionesListView, RegistroCapacitacionesListView, CrearCapacitaciones, ActualizarCapacitaciones, EliminarCapacitaciones
from .views.fichaPersonal.views import FichaPersonalTemplateView

app_name = "ficha_Personal"  # nombre de la app
urlpatterns = [
    path('fichaPersonal', FichaPersonalTemplateView.as_view(), name="fichaPersonal"),
    path('empleado', EmpleadoListView.as_view(), name='empleado'),
    path('crearempleado/', CrearEmpleado.as_view(), name='crearempleado'),
    path('actualizarempleado/<int:pk>/', ActualizarEmpleado.as_view(), name='actualizarempleado'),
    path('eliminarempleado/<int:pk>/', EliminarEmpleado.as_view(), name='deleteempleado'),

    path('cargo', CargoListView.as_view(), name='cargo'),
    path('crearcargo/', CrearCargo.as_view(), name='crearcargo'),
    path('actualizarcargo/<int:pk>/', ActualizarCargo.as_view(), name='actualizarcargo'),
    path('eliminarcargo/<int:pk>/', EliminarCargo.as_view(), name='deletecargo'),

    path('departamento', DepartamentoListView.as_view(), name='departamento'),
    path('creardepartamento/', CrearDepartamento.as_view(), name='creardepartamento'),
    path('actualizardepartamento/<int:pk>/', ActualizarDepartamento.as_view(), name='actualizardepartamento'),
    path('eliminardepartamento/<int:pk>/', EliminarDepartamento.as_view(), name='deletedepartamento'),

    path('contactoEmergencia', ContactoEmergenciaListView.as_view(), name='contactoEmergencia'),
    path('registroContactoEmergencia', RegistroContactoEmergenciaListView.as_view(), name='registroContactoEmergencia'),
    path('crearContactoEmergencia/', CrearContactoEmergencia.as_view(), name='crearContactoEmergencia'),
    path('actualizaContactoEmergencia/<int:pk>/', ActualizarContactoEmergencia.as_view(), name='actualizarContactoEmergencia'),
    path('eliminarContactoEmergencia/<int:pk>/', EliminarContactoEmergencia.as_view(), name='deleteContactoEmergencia'),

    path('infoAcademica', InfoAcademicaListView.as_view(), name='infoAcademica'),
    path('registroInfoAcademica', RegistroInfoAcademicaListView.as_view(), name='registroInfoAcademica'),
    path('crearInfoAcademica/', CrearInfoAcademica.as_view(), name='crearInfoAcademica'),
    path('actualizarInfoAcademica/<int:pk>/', ActualizarInfoAcademica.as_view(),name='actualizarInfoAcademica'),
    path('eliminarInfoAcademica/<int:pk>/', EliminarInfoAcademica.as_view(), name='deleteInfoAcademica'),

    path('capacitaciones', CapacitacionesListView.as_view(), name='capacitaciones'),
    path('registroCapacitaciones', RegistroCapacitacionesListView.as_view(), name='registroCapacitaciones'),
    path('crearCapacitaciones/', CrearCapacitaciones.as_view(), name='crearCapacitaciones'),
    path('actualizarCapacitaciones/<int:pk>/', ActualizarCapacitaciones.as_view(), name='actualizarCapacitaciones'),
    path('eliminarCapacitaciones/<int:pk>/', EliminarCapacitaciones.as_view(), name='deleteCapacitaciones'),
]
