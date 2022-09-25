from django.contrib import admin
from django.contrib.admin import AdminSite
from aplicaciones.ficha_personal.models import Empleado,ContactoEmergencias,Departamento,Cargo,InfoAcademica,Capacitaciones,Sueldo

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'cedula',
        'nombres',
        'ciudad',
        'direccion',
        'estado',
    )
    ordering = ('id',)
    search_fields = ('cedula', 'nombres',)
    list_filter = (
        'ciudad__nombre',
        'estado',
    )
admin.site.register(Empleado,EmpleadoAdmin)

class ContactoEmergenciaAdmin(admin.ModelAdmin):
    list_display = (
        'cedula',
        'nombre',
        'telefonos',
        'parentesco',
        'direccion',
    )
    ordering = ('id',)
    search_fields = ('cedula', 'nombre',)
    list_filter = (
        'nombre',
    )
admin.site.register(ContactoEmergencias,ContactoEmergenciaAdmin)

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = (
        'descripcion',
        'estado',
    )
    ordering = ('id',)
    list_filter = (
        'descripcion',
        'estado',
    )
admin.site.register(Departamento,DepartamentoAdmin)

class CargoAdmin(admin.ModelAdmin):
    list_display = (
        'descripcion',
        'estado',
    )
    ordering = ('id',)
    list_filter = (
        'descripcion',
        'estado',
    )
admin.site.register(Cargo,CargoAdmin)

class InfoAcademicaAdmin(admin.ModelAdmin):
    list_display = (
        'empleado',
        'fecha_Inicio',
        'fecha_Fin',
        'institucion',
        'titulo',
    )
    ordering = ('id',)
    search_fields = ('empleado',)
    list_filter = (
        'empleado',
    )
admin.site.register(InfoAcademica,InfoAcademicaAdmin)

class CapacitacionesAdmin(admin.ModelAdmin):
    list_display = (
        'empleado',
        'certificado',
        'fecha_Inicio',
        'fecha_Fin',
        'duracion',
    )
    ordering = ('id',)
    search_fields = ('empleado',)
    list_filter = (
        'empleado',
    )
admin.site.register(Capacitaciones,CapacitacionesAdmin)

class SueldoAdmin(admin.ModelAdmin):
    list_display = (
        'empleado',
        'fecha',
        'sueldo',
        'estado',
    )
    ordering = ('id',)
    search_fields = ('empleado',)
    list_filter = (
        'empleado',
    )
admin.site.register(Sueldo,SueldoAdmin)