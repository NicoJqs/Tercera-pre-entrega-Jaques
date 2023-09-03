from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    comision = forms.IntegerField()

class ProfesorForm(forms.Form):
    nombre = forms.CharField(max_length = 50)
    apellido = forms.CharField(max_length = 50)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=50)

class EstudiantesForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()

class EntregablesForm(forms.Form):
    nombre = forms.CharField(max_length = 50)
    fecha_entrega = forms.DateField()
    entregado = forms.BooleanField()

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(label= "Email")
    password1 = forms.CharField(label="contrasena", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contrasena", widget=forms.PasswordInput)

    class meta:
        model = User
        fields = ["username", "email", "passwor1", "password2"]
        help_text = {k:"" for k in fields}


class UserEditForm(UserCreationForm):

    email= forms.EmailField(label="Email Usuario")
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField(label='Modificar Nombre')
    last_name=forms.CharField(label='Modificar Apellido')
    
    class Meta:
        model=User
        fields=["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k:"" for k in fields}#para cada uno de los campos del formulario, le asigna un valor vacio


class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")