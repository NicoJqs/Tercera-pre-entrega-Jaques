from django.shortcuts import render
from .models import Curso, Profesor, Entregable, Estudiante, Avatar
from django.http import HttpResponse
from .forms import CursoForm, ProfesorForm, EstudiantesForm, EntregablesForm, RegistroUsuarioForm, UserEditForm, AvatarForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def obtenerAvatar(request):

    avatares=Avatar.objects.filter(user=request.user.id)
    
    if len(avatares)!=0:
        
        return avatares[0].imagen.url
    else:
        return "/media/avatars/avatarpordefecto.png"
    

def crear_curso(request):
    nombre_curso = "Programacion Basica"
    comision_curso = 99988
    print("Creando curso..")
    curso = Curso(nombre = nombre_curso, comision = comision_curso)
    curso.save()
    respuesta = f"Curso Creado: {curso.nombre} - {curso.comision}"
    return HttpResponse(respuesta)


@login_required
def listar_cursos(request):
    cursos = Curso.objects.all()
    respuesta = ""
    for curso in cursos:
        respuesta += f"Curso: {curso.nombre} | Comision: {curso.comision}<br>"
    return HttpResponse(respuesta)


def inicio(request):
    avatar= obtenerAvatar(request)   
    return render(request,"AppCoder/inicio.html", {"avatar":obtenerAvatar(request)})

@login_required
def profesores(request):
    avatar= obtenerAvatar(request)
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
            mensaje = "Profesor creado."
        else:
            mensaje = "Datos invalidos."
        profesores = Profesor.objects.all()
        formulario_profesor = ProfesorForm()
        return render(request, "AppCoder/profesores.html",{"mensaje":mensaje, "formulario":formulario_profesor, "profesores": profesores, "profesores":profesores, "avatar":avatar})
    else:
        formulario_profesor=ProfesorForm()
        profesores = Profesor.objects.all()

    return render(request,"AppCoder/profesores.html", {"formulario":formulario_profesor, "profesores": profesores, "profesores":profesores, "avatar":avatar})

@login_required
def eliminarProfesor(request, id):
    profesor = Profesor.objects.get(id = id)
    profesor.delete()
    profesores = Profesor.objects.all()
    formulario_profesor = ProfesorForm()
    mensaje = "Profesor eliminado."
    return render(request,"AppCoder/profesores.html", {"mensaje":mensaje,"formulario":formulario_profesor, "profesores": profesores})

@login_required
def editarProfesor(request,id):
    profesor = Profesor.objects.get(id = id)
    if request.method=="POST":
        form = ProfesorForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            profesor.nombre=info["nombre"]
            profesor.apellido=info["apellido"]
            profesor.email=info["email"]
            profesor.profesion=info["profesion"]

            profesor.save()
            mensaje = "Profesor editado."
            profesores = Profesor.objects.all()
            formulario_profesor = ProfesorForm()
            return render(request, "AppCoder/profesores.html",{"mensaje":mensaje, "formulario":formulario_profesor, "profesores": profesores})
    else:
        formulario_profesor = ProfesorForm(initial={"nombre": profesor.nombre, "apellido":profesor.apellido, "email":profesor.email, "profesion":profesor.profesion})
        return render(request,"AppCoder/editarProfesor.html", {"formulario":formulario_profesor, "profesor": profesor})


class EstudianteList(LoginRequiredMixin, ListView):
    model = Estudiante
    template_name = "AppCoder/estudiantes.html"

class EstudianteCreacion(LoginRequiredMixin, CreateView):
    model = Estudiante
    success_url = reverse_lazy("estudiante_list")
    fields = ['nombre', 'apellido', 'email']

class EstudianteDetalle(LoginRequiredMixin, DetailView):
    model = Estudiante
    template_name = "AppCoder/estudiante_detalle.html"

class EstudianteDelete(LoginRequiredMixin, DeleteView):
    model = Estudiante
    success_url = reverse_lazy("estudiante_list")
    
class EstudianteUpdate(LoginRequiredMixin, UpdateView):
    model = Estudiante
    success_url = reverse_lazy("estudiante_list")
    fields = ['nombre', 'apellido', 'email']

@login_required
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

@login_required
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

def login_request(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info = form.cleaned_data
            usu = info["username"]
            clave = info["password"]
            usuario = authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppCoder/inicio.html", {"mensaje":f"Usuario {usu} Logueado correctamente"})
            else:
                return render(request, "AppCoder/login.html", {"form":form, "mensaje": "Datos invalidos."})
        else:
            return render(request, "AppCoder/login.html", {"form":form, "mensaje": "Datos invalidos."})
    else:
        form = AuthenticationForm()
        return render(request, "AppCoder/login.html", {"form": form})

def register(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            nombre_usuario = info["username"]
            form.save()
            return render(request, "AppCoder/inicio.html", {"mensaje":f"Usuario {nombre_usuario} creado correctamente."})
    else:
        form = RegistroUsuarioForm()
        return render(request, "AppCoder/register.html", {"form":form})
    
@login_required
def editarPerfil(request):
    usuario=request.user

    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "AppCoder/inicio.html", {"mensaje":f"Usuario {usuario.username} editado correctamente"})
        else:
            return render(request, "AppCoder/editarPerfil.html", {"form": form, "nombreusuario":usuario.username, "mensaje":"Datos invalidos"})
    else:
        form=UserEditForm(instance=usuario)
        return render(request, "AppCoder/editarPerfil.html", {"form": form, "nombreusuario":usuario.username})
    
@login_required
def agregarAvatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])#antes de guardarlo, tengo q hacer algo
            
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render(request, "AppCoder/inicio.html", {"mensaje":f"Avatar agregado correctamente", "avatar":obtenerAvatar(request)})
        else:
            return render(request, "AppCoder/agregarAvatar.html", {"form": form, "usuario": request.user, "mensaje":"Error al agregar el avatar"})
    else:
        form=AvatarForm()
        return render(request, "AppCoder/agregarAvatar.html", {"form": form, "usuario": request.user, "avatar":obtenerAvatar(request)})