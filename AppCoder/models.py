from django.db import models
from django.contrib.auth.models import User


class Curso(models.Model):
    nombre = models.CharField(max_length = 50)
    comision = models.IntegerField()
    def __str__(self):
        return f"{self.nombre} - {self.comision}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    email = models.EmailField()
    def __str__(self):
        return f"{self.apellido} {self.nombre} - {self.email}"


class Profesor(models.Model):
    nombre = models.CharField(max_length = 50)
    apellido = models.CharField(max_length = 50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.apellido} {self.nombre} - {self.email} | {self.profesion}"


class Entregable(models.Model):
    nombre = models.CharField(max_length = 50)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()
    def __str__(self):
        return f"Trabajo Practico: {self.nombre} - Fecha de Entrega: {self.fecha_entrega} Entregado: {self.entregado}"


class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatars",null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)