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