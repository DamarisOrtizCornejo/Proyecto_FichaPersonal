from django.db import models
from django.urls import reverse

from aplicaciones.core.models import Base, Pais, Provincia, Ciudad
from proyecto_administrativo import settings
from aplicaciones.ficha_personal.constantes import Opciones

opciones = Opciones()
GENERO = opciones.genero()
ESTADO_CIVIL = opciones.estado_civil()
TIPO_CONTRATO = opciones.tipo_contrato()
PARENTESCO = opciones.parentesco()

class Cargo(models.Model):
    descripcion = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "{}".format(self.descripcion)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"
        ordering = ('id',)

class Departamento(models.Model):
    descripcion = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "{}".format(self.descripcion)

    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"
        ordering = ('id',)


class Empleado(Base):
    nombres = models.CharField(max_length=200)
    cedula = models.CharField(max_length=10, unique=True)
    fecha_nacimiento = models.DateField(blank=True, null=True, auto_now=False)
    genero = models.CharField(max_length=1, choices=GENERO, default=GENERO[0][0], blank=True, null=True)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT, blank=True, null=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT, blank=True, null=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT, blank=True, null=True)
    estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIL, default=ESTADO_CIVIL[0][0], blank=True,null=True)
    email = models.CharField(max_length=100, unique=True)
    direccion = models.TextField(blank=True, null=True, verbose_name='Dirección')
    telefonos = models.CharField(max_length=50, blank=True, null=True)
    fecha_IESS = models.DateField(blank=True, null=True, auto_now=False)
    tipo_Contrato = models.CharField(max_length=2, choices=TIPO_CONTRATO, default=TIPO_CONTRATO[0][0], blank=True,null=True)
    fecha_Ingreso = models.DateField(blank=True, null=True, auto_now=False)
    # sueldo = models.ForeignKey(Ciudad, on_delete=models.PROTECT, blank=True, null=True)
    foto = models.ImageField(upload_to='fichaPersonal/empleados', blank=True, null=True)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT,blank=True, null=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT,blank=True, null=True)
    estado = models.BooleanField(default=True)


    def __str__(self):
        return "{} - {}".format(self.cedula, self.nombres)

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ('id',)

    def get_image(self):
        if self.foto:
            return '{}{}'.format(settings.MEDIA_URL, self.foto)
        return '{}{}'.format(settings.STATIC_URL, 'img/default/empty.jpg')

    def estadoCivil(self):
        if self.estado_civil=="S":
           estado="Soltero(a)"
        elif self.estado_civil=="C":
            estado="Casado(a)"
        elif self.estado_civil=="D":
            estado="Divorciado(a)"
        elif self.estado_civil=="V":
            estado="Viudo(a)"
        else:
            estado="Union Libre"
        return estado

class ContactoEmergencias(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT,blank=True, null=True, related_name="contactos")
    nombre = models.CharField(max_length=200)
    cedula = models.CharField(max_length=10, unique=True)
    telefonos = models.CharField(max_length=50, blank=True, null=True)
    parentesco = models.CharField(max_length=2, choices=PARENTESCO, default=PARENTESCO[0][0], blank=True, null=True)
    direccion = models.TextField(blank=True, null=True, verbose_name='Dirección')

    def __str__(self):
        return "{} - {}".format(self.cedula, self.nombre)

    class Meta:
        verbose_name = "ContactoEmergencia"
        verbose_name_plural = "ContactosEmergencias"
        ordering = ('id',)

    def pariente(self):
        if self.parentesco=="M":
           paren="Madre"
        elif self.parentesco=="P":
            paren="Padre"
        elif self.parentesco=="H":
            paren="Hermano(a)"
        elif self.parentesco=="A":
            paren="Abuelo(a)"
        elif self.parentesco=="T":
            paren="Tio(a)"
        elif self.parentesco=="Pr":
            paren="Primo(a)"
        elif self.parentesco=="S":
            paren="Sobrino(a)"
        elif self.parentesco=="C":
            paren="Cuñado(a)"
        elif self.parentesco=="Pd":
            paren="Padrastro"
        elif self.parentesco=="Md":
            paren="Madrastra"
        elif self.parentesco=="Co":
            paren="Conyuge"
        elif self.parentesco=="Hi":
            paren="Hijo(a)"
        else:
            paren="Otros"
        return paren

class InfoAcademica(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT, blank=True, null=True)
    fecha_Inicio = models.DateField(blank=True, null=True, auto_now=False)
    fecha_Fin = models.DateField(blank=True, null=True, auto_now=False)
    institucion = models.CharField(max_length=100, blank=True, null=True)
    titulo = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.institucion)

    class Meta:
        verbose_name = "InfoAcademica"
        verbose_name_plural = "InfoAcademicas"
        ordering = ('id',)

class Capacitaciones(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT, blank=True, null=True)
    certificado = models.FileField(upload_to='fichaPersonal/capacitaciones', blank=True, null=True)
    fecha_Inicio = models.DateField(blank=True, null=True, auto_now=False)
    fecha_Fin = models.DateField(blank=True, null=True, auto_now=False)
    duracion = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.id)

    class Meta:
        verbose_name = "Capacitacion"
        verbose_name_plural = "Capacitaciones"
        ordering = ('id',)

    def get_file(self):
        if self.certificado:
            return '{}{}'.format(settings.MEDIA_URL, self.certificado)
        return '{}{}'.format(settings.STATIC_URL, 'Archivo sin subir')

class Sueldo(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True, auto_now=False)
    sueldo = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Sueldo')
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.sueldo)

    class Meta:
        verbose_name = "Sueldo"
        verbose_name_plural = "Sueldos"
        ordering = ('id',)
