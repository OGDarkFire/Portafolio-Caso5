from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.urls import reverse
# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('is admin', default=False)
    is_customer = models.BooleanField('is customer', default=False)
    is_employee = models.BooleanField('is employee', default=False)
    is_Uni1= models.BooleanField('Unidad 1', default=False)
    is_Uni2 = models.BooleanField('Unidad 2', default=False)
    is_Uni3 = models.BooleanField('Unidad 3', default=False)
    is_Jer1= models.BooleanField('Jefe', default=False)
    is_Jer2 = models.BooleanField('Supervisor', default=False)
    is_Jer3 = models.BooleanField('Empleado', default=False)

    def get_admin(self):
        admin = None
        if hasattr(self, 'admin'):
            admin = self.admin
        return admin

    def get_customer(self):
        customer = None
        if hasattr(self, 'customer'):
            customer = self.customer
        return customer

    def get_employee(self):
        employee = None
        if hasattr(self, 'employee'):
            employee = self.employee
        return employee

    class Meta:
            db_table = 'auth_user'

class Unidad(models.Model):
    Nombre_U = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre_U

class Rol(models.Model):
    Nombre_R = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre_R

class Jerarquia(models.Model):
    Nombre_J = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre_J

class Usuario(models.Model):
    ADMIN = 1
    CUSTOMER = 2
    EMPLOYEE = 3

    ROLE_CHOICES = (
        (ADMIN, 'admin'),
        (CUSTOMER, 'customer'),
        (EMPLOYEE, 'employee')
    )

    Unidad_1 = 1
    Unidad_2 = 2
    Unidad_3 = 3

    ROLE_CHOICES2 = (
        (Unidad_1, 'Unidad 1'),
        (Unidad_2, 'Unidad 2'),
        (Unidad_3, 'Unidad 3')
    )

    Nombre = models.OneToOneField(User, on_delete=models.CASCADE)
    Rol = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=0)
    Unidad = models.PositiveSmallIntegerField(choices=ROLE_CHOICES2, blank=True, null=True, default=0)

    def __str__(self):
            return str(self.Nombre)

class Tarea(models.Model):
    Nombre_Tarea = models.CharField(max_length=50)
    Responsable = models.ForeignKey(User, on_delete=models.CASCADE)
    Fecha_desde = models.DateField()
    Fecha_hasta = models.DateField()
    Descripcion = models.TextField()
    completado = models.BooleanField(default=False)

    def __str__(self):
        return self.Nombre_Tarea

class Tarea2(models.Model):
    NombreTa = models.ForeignKey(Tarea, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
            return str(self.NombreTa)

class TareaAce(models.Model):
    Nom_Ta = models.ForeignKey(Tarea2, on_delete=models.CASCADE, blank=True, null=True)
    TareaAce = models.ManyToManyField(Tarea,blank=True, null=True)

    def __str__(self):
        return str(self.TareaAce)
    def get_absolute_url(self, ):
        return reverse('detail',args=[self.id])

class TareaSub(models.Model):
    Nombre_TareaS = models.CharField(max_length=50)
    ResponsableS = models.ForeignKey(User, on_delete=models.CASCADE)
    TareaMadreS = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    Fecha_desdeS = models.DateField()
    Fecha_hastaS = models.DateField()
    DescripcionS = models.TextField()

    def __str__(self):
        return str(self.Nombre_TareaS)

class Atraso(models.Model):
    Revision = 1
    Respondido = 2

    Estado = (
        (Revision, 'Revision'),
        (Respondido, 'Respondido'),
    )
    Nombre_Responsable = models.CharField(max_length=50)
    Nombre_Tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    Estado = models.PositiveSmallIntegerField(choices=Estado, blank=True, null=True, default=1)
    Mensaje = models.TextField()

    def __str__(self):
            return str(self.Nombre_Responsable)

class Problema(models.Model):
    Asignacion_Tarea = 1
    Fechas = 2
    Reclamo = 3
    Sugerencia = 4
    Otro = 5

    TipoProblema = (
        (Asignacion_Tarea, 'Asignacion Tarea'),
        (Fechas, 'Fechas'),
        (Reclamo, 'Reclamo'),
        (Sugerencia, 'Sugerencia Tarea'),
        (Otro, 'Otro'),
    )

    Revision = 1
    Respondido = 2
    Cerrado = 3

    Estado = (
        (Revision, 'Revision'),
        (Respondido, 'Respondido'),
        (Cerrado, 'Cerrado'),
    )
    Nombre = models.CharField(max_length=50)
    TipoProblema = models.PositiveSmallIntegerField(choices=TipoProblema, blank=True, null=True, default=0)
    Estado = models.PositiveSmallIntegerField(choices=Estado, blank=True, null=True, default=1)
    Mensaje = models.TextField()

    def __str__(self):
            return str(self.Nombre)

