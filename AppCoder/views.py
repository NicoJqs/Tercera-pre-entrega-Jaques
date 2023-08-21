from django.shortcuts import render
from .models import Curso, Profesor, Estudiante, Entregable
from django.http import HttpResponse
from .forms import CursoForm, ProfesorForm, EstudiantesForm, EntregablesForm

# Create your views here.
def crear_curso(request):

    nombre_curso = "Programacion Basica"
    comision_curso = 99988
    print("Creando curso..")
    curso = Curso(nombre = nombre_curso, comision = comision_curso)
    curso.save()
    respuesta = f"Curso Creado: {curso.nombre} - {curso.comision}"
    return HttpResponse(respuesta)

def listar_cursos(request):
    cursos = Curso.objects.all()
    respuesta = ""
    for curso in cursos:
        respuesta += f"Curso: {curso.nombre} | Comision: {curso.comision}<br>"
    return HttpResponse(respuesta)

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def profesores(request):
    if request.method=="POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre=info["nombre"]
            apellido=info["apellido"]
            email=info["email"]
            profesion=info["profesion"]
            profesor = Profesor(nombre=nombre,apellido=apellido,email=email,profesion=profesion)
            profesor.save()
            return render(request,"AppCoder/profesores.html", {"mensaje":"Profesor Creado."})
        else:
            return render(request,"AppCoder/profesores.html", {"mensaje":"Datos Invalidos."})
    else:
        formulario_profesor = ProfesorForm()
    return render(request, "AppCoder/profesores.html", {"formulario":formulario_profesor})


def estudiantes(request):
    if request.method=="GET":
        form = EstudiantesForm(request.GET)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info["nombre"]
            apellido = info["apellido"]
            email = info["email"]
            estudiante = Estudiante(nombre=nombre, apellido=apellido, email=email)
            estudiante.save()
            return render(request, "AppCoder/estudiantes.html", {"mensaje":"Alumno Creado."})
        else:
            formulario_estudiante = EstudiantesForm()
        return render(request, "AppCoder/estudiantes.html", {"formulario":formulario_estudiante})
    
def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    respuesta = ""
    for estudiante in estudiantes:
        respuesta += f"{estudiante.id} - {estudiante.apellido} {estudiante.nombre} {estudiante.email}<br>"
    return HttpResponse(respuesta)


def entregables(request):
    if request.method=="GET":
        form = EntregablesForm(request.GET)
        if form.is_valid():
            info = form.cleaned_data
            nombre = info["nombre"]
            fecha_entrega=info["fecha_entrega"]
            entregado = info["entregado"]
            entrega = Entregable(nombre = nombre, fecha_entrega=fecha_entrega, entregado = entregado)
            entrega.save()
            return render(request, "AppCoder/entregables.html", {"mensaje":"Entregable creado."})
        else:
            formulario_entregable = EntregablesForm()
        return render(request, "AppCoder/entregables.html", {"formulario": formulario_entregable})

def cursos(request):
    if request.method=="POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre"]
            comision=info["comision"]
            curso = Curso(nombre = nombre, comision = comision)
            curso.save()
            return render(request, "AppCoder/cursos.html", {"mensaje":"Curso creado"})
        return render(request, "AppCoder/cursos.html", {"mensaje":"Datos Invalidos"})
    else:
        formulario_curso = CursoForm()
        return render(request, "AppCoder/cursos.html", {"formulario": formulario_curso})
    

def busquedaComision(request):
    return render(request, "AppCoder/busquedaComision.html")

def buscar(request):
    comision = request.GET["comision"]
    if comision != "":
        cursos = Curso.objects.filter(comision=comision)
        return render(request, "AppCoder/resultadosBusqueda.html", {"cursos": cursos})
    else:
        return render(request, "AppCoder/busquedaComision.html", {"mensaje": "Error: Ingresar algun dato!"})



def busquedaEstudiantes(request):
    return render(request, "AppCoder/busquedaEstudiantes.html")

def buscarEstudiantes(request):
    nombre = request.GET['nombre']
    if nombre:
        estudiantes = Estudiante.objects.filter(nombre__icontains=nombre)
        return render(request, "AppCoder/resultadosBusquedaEstudiantes.html", {"estudiantes": estudiantes})
    else:
        return render(request, "AppCoder/busquedaEstudiantes.html", {"mensaje": "Error: Ingresar algún nombre válido."})
