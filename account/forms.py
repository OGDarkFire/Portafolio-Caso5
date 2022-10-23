from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Usuario, Unidad, Rol, Jerarquia, Tarea, TareaSub, TareaAce, Tarea2

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_admin', 'is_employee', 'is_customer')

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

class UnidadForm(forms.ModelForm):
    class Meta:
        model = Unidad
        fields = '__all__'

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = '__all__'

class JerarquiaForm(forms.ModelForm):
    class Meta:
        model = Jerarquia
        fields = '__all__'

class TareasForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = '__all__'

        widgets = {
            "Fecha_desde": forms.SelectDateWidget(),
            "Fecha_hasta": forms.SelectDateWidget()
        }

class TareasSubForm(forms.ModelForm):
    class Meta:
        model = TareaSub
        fields = '__all__'

        widgets = {
            "Fecha_desdeS": forms.SelectDateWidget(),
            "Fecha_hastaS": forms.SelectDateWidget()
        }

class TareaAForm(forms.ModelForm):
    class Meta:
        model = TareaAce
        fields = '__all__'

class Tarea2Form(forms.ModelForm):
    class Meta:
        model = Tarea2
        fields = '__all__'