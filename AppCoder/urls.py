from django.urls import path
from .views import *

urlpatterns = [
    path('crear_curso', crear_curso),
    path('listar_cursos', listar_cursos),
    path('profesores', profesores, name="profesores"),
    path('estudiantes', estudiantes, name="estudiantes"),
    path('lista_estudiantes', listar_estudiantes),
    path('cursos', cursos, name="cursos"),
    path('entregables', entregables, name="entregables"),
    path('busquedaComision', busquedaComision, name="busquedaComision"),
    path('buscar', buscar, name="buscar"),
    path('resultadosBusqueda', buscar, name="resultadosBusqueda"),
    path('busquedaEstudiantes', busquedaEstudiantes, name="busquedaEstudiantes"),
    path('buscarEstudiantes', buscarEstudiantes, name="buscarEstudiantes"),
    path('resultadosBusquedaEstudiantes', buscarEstudiantes, name="resultadosBusquedaEstudiantes")
]