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
    path('resultadosBusquedaEstudiantes', buscarEstudiantes, name="resultadosBusquedaEstudiantes"),
    path('eliminarProfesor/<id>', eliminarProfesor, name="eliminarProfesor"),
    path('editarProfesor/<id>', editarProfesor, name="editarProfesor"),

    path('estudiante/list/', EstudianteList.as_view(), name="estudiante_list"),
    path('estudiante/nuevo/', EstudianteCreacion.as_view(), name="estudiante_crear"),
    path('estudiante/detalle/<pk>', EstudianteDetalle.as_view(), name="estudiante_detalle"),
    path('estidiante/borrar/<pk>', EstudianteDelete.as_view(), name="estudiante_borrar"),
    path('estudiante/editar/<pk>', EstudianteUpdate.as_view(), name="estudiante_editar"),

    path('login/', login_request, name="login"),
    path('register/', register, name="register"),
]