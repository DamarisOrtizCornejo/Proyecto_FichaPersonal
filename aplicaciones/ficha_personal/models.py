from django.db import models
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
    fecha_nacimiento = models.DateField(blank=True, null=True)
    genero = models.CharField(max_length=1, choices=GENERO, default=GENERO[0][0], blank=True, null=True)
    pais = models.ForeignKey(Pais, on_delete=models.PROTECT, blank=True, null=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT, blank=True, null=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.PROTECT, blank=True, null=True)
    estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIL, default=ESTADO_CIVIL[0][0], blank=True,null=True)
    email = models.CharField(max_length=100, unique=True)
    direccion = models.TextField(blank=True, null=True, verbose_name='Dirección')
    telefonos = models.CharField(max_length=50, blank=True, null=True)
    fecha_IESS = models.DateField(blank=True, null=True)
    tipo_Contrato = models.CharField(max_length=2, choices=TIPO_CONTRATO, default=TIPO_CONTRATO[0][0], blank=True,null=True)
    fecha_Ingreso = models.DateField(blank=True, null=True)
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


class ContactoEmergencias(Base):
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT, blank=True, null=True)
    nombres = models.CharField(max_length=200)
    cedula = models.CharField(max_length=10, unique=True)
    telefonos = models.CharField(max_length=50, blank=True, null=True)
    parentesco = models.CharField(max_length=2, choices=PARENTESCO, default=PARENTESCO[0][0], blank=True, null=True)
    direccion = models.TextField(blank=True, null=True, verbose_name='Dirección')

    def __str__(self):
        return "{} - {}".format(self.cedula, self.nombres)

    class Meta:
        verbose_name = "ContactoEmergencia"
        verbose_name_plural = "ContactosEmergencias"
        ordering = ('id',)

class InfoAcademica(Base):
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT, blank=True, null=True)
    fecha_Inicio = models.DateField(blank=True, null=True)
    fecha_Fin = models.DateField(blank=True, null=True)
    institucion = models.CharField(max_length=10, unique=True)
    titulo = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return "{}".format(self.empleado)

    class Meta:
        verbose_name = "InfoAcademica"
        verbose_name_plural = "InfoAcademicas"
        ordering = ('id',)


class Capacitaciones(Base):
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT, blank=True, null=True)
    certificado = models.FileField(upload_to='fichaPersonal/capacitaciones', blank=True, null=True)
    fecha_Inicio = models.DateField(blank=True, null=True)
    fecha_Fin = models.DateField(blank=True, null=True)
    duracion = models.CharField(max_length=10, unique=True)

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


class Sueldo(Base):
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    sueldo = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Sueldo')

    def __str__(self):
        return "{}".format(self.sueldo)

    class Meta:
        verbose_name = "Sueldo"
        verbose_name_plural = "Sueldos"
        ordering = ('id',)


