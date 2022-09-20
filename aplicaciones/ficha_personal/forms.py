from django import forms
from django.forms import ModelForm

from aplicaciones.core.models import Pais
from aplicaciones.ficha_personal.models import Cargo,Departamento,Empleado,ContactoEmergencias,InfoAcademica,Capacitaciones

class CargoForm(ModelForm):
    class Meta:
        model = Cargo
        fields = ['descripcion', 'estado']
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Ingrese Cargo','required': True}),
        }

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['descripcion', 'estado']
        widgets = {
            'descripcion': forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Ingrese Departamento','required': True}),
        }

class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Ingrese Nombre Completo'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese Cédula'}),
            'fecha_nacimiento': forms.DateInput(format=('%d/%m/%Y'),
                                                attrs={'class': 'form-control', 'placeholder': 'Ingrese su Fecha de Nacimiento', 'type': 'date'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'pais': forms.Select(attrs={'class': 'form-control'}),
            'provincia': forms.Select(attrs={'class': 'form-control'}),
            'ciudad': forms.Select(attrs={'class': 'form-control'}),
            'estado_civil': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Ingrese Email'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese Dirección'}),
            'telefonos': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese Teléfono'}),
            'fecha_IESS': forms.DateInput(format=('%d/%m/%Y'),
                                                attrs={'class': 'form-control', 'placeholder': 'Seleccione una fecha','type': 'date'}),
            'tipo_Contrato': forms.Select(attrs={'class': 'form-control'}),
            'fecha_Ingreso': forms.DateInput(format=('%d/%m/%Y'),
                                          attrs={'class': 'form-control', 'placeholder': 'Seleccione una fecha','type': 'date'}),
            'cargo': forms.Select(attrs={'class': 'form-control'}),
            'departamento': forms.Select(attrs={'class': 'form-control'}),
            # 'sueldo': forms.fo(attrs={'class': 'form-control'}),
            # 'foto': forms.ImageField(attrs={'class': 'form-control'}),
            # 'fecha': forms.DateInput(attrs={'class': 'form-control'}),
        }

class PaisForm(ModelForm):
    class Meta:
        model = Pais
        fields = '__all__'

        widgets = {
           'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ContactoEmergenciasForm(ModelForm):
    class Meta:
        model = ContactoEmergencias
        fields = '__all__'
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control','placeholder' : 'Ingrese nombre'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese su número de cédula'}),
            'telefonos': forms.TextInput(attrs={'class': 'form-control','placeholder':'Número celular'}),
            'parentesco': forms.Select(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese Dirección'}),
        }

class InfoAcademicaForm(ModelForm):
    class Meta:
        model = InfoAcademica
        fields = '__all__'
        widgets = {
            'fecha_Inicio': forms.DateInput(format=('%d/%m/%Y'),attrs={'class': 'form-control', 'placeholder': 'Seleccione una fecha','type': 'date'}),
            'fecha_Fin': forms.DateInput(format=('%d/%m/%Y'),attrs={'class': 'form-control', 'placeholder': 'Seleccione una fecha','type': 'date'}),
            'institucion': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese su institución'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control','placeholder':'Titulo obtenido'}),
        }

class CapacitacionesForm(ModelForm):
    class Meta:
        model = Capacitaciones
        fields = '__all__'
        widgets = {
            #'certificado': forms.FileField(),
            'fecha_Inicio': forms.DateInput(format=('%d/%m/%Y'),attrs={'class': 'form-control', 'placeholder': 'Seleccione la fecha inicial','type': 'date'}),
            'fecha_Fin': forms.DateInput(format=('%d/%m/%Y'),attrs={'class': 'form-control', 'placeholder': 'Seleccione la fecha final','type': 'date'}),
            'duracion': forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese cuanto tiempo duro su capacitacion'}),
        }