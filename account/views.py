from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from .forms import *
from .models import *
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')
            elif user is not None and user.is_employee:
                login(request, user)
                return redirect('employee')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'A ocurrido un problema'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def admin(request):
    return render(request,'admin.html')

def Listar_Problema(request):
    problemas = Problema.objects.all()
    data = {
        'problemas':problemas
    }
    return render(request,'Lista_Problema/lista.html',data)

def Listar_Atraso(request):
    atrasos = Atraso.objects.all()
    data = {
        'atrasos':atrasos
    }
    return render(request,'Lista_Atraso/lista.html',data)
#def customer(request):
#    return render(request,'customer.html')

#def employee(request):
 #   Tareasa = TareaAce.objects.all()
  #  return render(request, 'employee.html', {'Tareasa':Tareasa})

def detail_page(request,id):
    obj=TareaAce.objects.get(id=id)
    return render(request, 'detail.html',{'obj':obj})

def customer(request):
    tareas = Tarea.objects.all()
    data = {
        'tareas':tareas
    }
    return render(request,'customer.html',data)

def TerminarTarea(request, id): 
    tareas = Tarea.objects.get(id=id)
    form = TareasForm(instance=tareas)
    if request.method == "POST":
        form = TareasForm(request.POST, instance=tareas)
        if form.is_valid():
            form.save()
            return redirect(to="customer")

    context = {'form': form}
    return render(request, 'TareasFun/terminar_tarea.html', context)

def Listar_TareaF(request): 
    tareas = Tarea.objects.all()
    data = {
        'tareas':tareas
    }
    return render(request,'Estado/TareasFin.html',data)

def Listar_TareaP(request): 
    tareas = Tarea.objects.all()
    data = {
        'tareas':tareas
    }
    return render(request,'Estado/TareasProcc.html',data)

def TareaA(request):
    Tareasa = TareaAce.objects.all()
    return render(request, 'TareaA/Listar.html', {'Tareasa':Tareasa})

#Comienzo Usuario Admin

def AgregarUsuario(request):
    data = {
        'form': UsuarioForm()       
    }
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data["form"] = formulario
    return render(request,'CrudAdmin/agregar.html', data)

def ListarUsuario(request):
    Usuarios = Usuario.objects.all()
    data = {
        'Usuarios': Usuarios
    }
    return render(request, 'CrudAdmin/listar.html', data)

def ModificarUsuario(request, id):
    usuario = get_object_or_404 (Usuario,id=id)
    data = {
        'form': UsuarioForm(instance=usuario)
    }

    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="ListarUsuario")
        data["form"] = formulario

    return render(request, 'CrudAdmin/Modificar.html', data)

def EliminarUsuario(request,id):
    usuario = get_object_or_404(Usuario,id=id)
    usuario.delete()
    return redirect(to="ListarUsuario")

#Fin Tareas Admin

#Comienzo Tareas Rechazadas
def AgregarTR(request):
    data = {
        'form': EstadoForm()       
    }
    if request.method == 'POST':
        formulario = EstadoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data["form"] = formulario
    return render(request,'TareasR/agregarT.html', data)

def ListarT(request):
    TareasR = Estado_Tarea.objects.all()
    data = {
        'TareasR': TareasR
    }
    return render(request, 'TareasR/listaTareas.html', data)

def ModificarT(request, id):
    tareasR = get_object_or_404 (Estado_Tarea,id=id)
    data = {
        'form': EstadoForm(instance=tareasR)
    }

    if request.method == 'POST':
        formulario = EstadoForm(data=request.POST, instance=tareasR)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="ListarT")
        data["form"] = formulario

    return render(request, 'TareasR/ModificarT.html', data)

def EliminarT(request,id):
    tareasR = get_object_or_404(Estado_Tarea,id=id)
    tareasR.delete()
    return redirect(to="ListarT")

#Fin Tareas Rechazadas

def AgregarUnidad(request):
    data = {
        'form': UnidadForm()
    }
    if request.method == 'POST':
        formulario = UnidadForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data["form"] = formulario
    return render(request,'CrudUni/agregar.html', data)

def ListarUnidad(request):
    Unidads = Unidad.objects.all()
    data = {
        'Unidads': Unidads
    }
    return render(request, 'CrudUni/listar.html', data)


def ModificarUnidad(request, id):
    unidad = get_object_or_404 (Unidad,id=id)
    data = {
        'form': UnidadForm(instance=unidad)
    }

    if request.method == 'POST':
        formulario = UnidadForm(data=request.POST, instance=unidad)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="ListarUnidad")
        data["form"] = formulario

    return render(request, 'CrudUni/modificar.html', data)

def EliminarUnidad(request,id):
    unidad = get_object_or_404(Unidad,id=id)
    unidad.delete()
    return redirect(to="ListarUnidad")
#Fin Unidad

#Comienzo Rol
def AgregarRol(request):
    data = {
        'form': RolForm()
    }
    if request.method == 'POST':
        formulario = RolForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data["form"] = formulario
    return render(request,'CrudRo/agregar.html', data)

def ListarRol(request):
    Rols = Rol.objects.all()
    data = {
        'Rols': Rols
    }
    return render(request, 'CrudRo/listar.html', data)


def ModificarRol(request, id):
    rol = get_object_or_404 (Rol,id=id)
    data = {
        'form': RolForm(instance=rol)
    }

    if request.method == 'POST':
        formulario = RolForm(data=request.POST, instance=rol)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Rol Modificado Correctamente")
            return redirect(to="ListarRol")
        data["form"] = formulario

    return render(request, 'CrudRo/modificar.html', data)

def EliminarRol(request,id):
    rol = get_object_or_404(Rol,id=id)
    rol.delete()
    return redirect(to="ListarRol")
#Fin Rol

#Comienzo Jerarquia
def AgregarJerarquia(request):
    data = {
        'form': JerarquiaForm()
    }
    if request.method == 'POST':
        formulario = JerarquiaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data["form"] = formulario
    return render(request,'CrudJer/agregar.html', data)

def ListarJerarquia(request):
    Jerarquias = Jerarquia.objects.all()
    data = {
        'Jerarquias': Jerarquias
    }
    return render(request, 'CrudJer/listar.html', data)


def ModificarJerarquia(request, id):
    jerarquia = get_object_or_404 (Jerarquia,id=id)
    data = {
        'form': JerarquiaForm(instance=jerarquia)
    }

    if request.method == 'POST':
        formulario = JerarquiaForm(data=request.POST, instance=jerarquia)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="ListarJerarquia")
        data["form"] = formulario

    return render(request, 'CrudJer/modificar.html', data)

def EliminarJerarquia(request,id):
    jerarquia = get_object_or_404(Jerarquia,id=id)
    jerarquia.delete()
    return redirect(to="ListarJerarquia")
#Comienzo Jerarquia

#Comienzo Tareas Funcionario

def employee(request):
    Tareas = Tarea.objects.all()
    data = {
        'Tareas': Tareas
    }
    return render(request, 'employee.html', data)
    
def AgregarTarea(request):
    data = {
        'form': TareasForm()
    }
    if request.method == 'POST':
        formulario = TareasForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data["form"] = formulario
    return render(request,'TareasFun/agregar.html', data)


def ModificarTarea(request, id):
    tarea = get_object_or_404 (Tarea,id=id)
    data = {
        'form': TareasForm(instance=tarea)
    }

    if request.method == 'POST':
        formulario = TareasForm(data=request.POST, instance=tarea)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="employee")
        data["form"] = formulario

    return render(request, 'TareasFun/Modificar.html', data)

def EliminarTarea(request,id):
    tarea = get_object_or_404(Tarea,id=id)
    tarea.delete()
    return redirect(to="employee")

#Fin Tareas Funcionario

#Comienzo Tareas Subordinadas Funcionario
def AgregarTareaSub(request):
    data = {
        'form': TareasSubForm()
    }
    if request.method == 'POST':
        formulario = TareasSubForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data["form"] = formulario
    return render(request,'TareasSub/agregar.html', data)

def ListarTareaSub(request):
    Tareassub = TareaSub.objects.all()
    data = {
        'Tareassub': Tareassub
    }
    return render(request, 'TareasSub/listar.html', data)


def ModificarTareaSub(request, id):
    tareasub = get_object_or_404 (TareaSub,id=id)
    data = {
        'form': TareasSubForm(instance=tareasub)
    }

    if request.method == 'POST':
        formulario = TareasSubForm(data=request.POST, instance=tareasub)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="ListarTareaSub")
        data["form"] = formulario

    return render(request, 'TareasSub/modificar.html', data)

def EliminarTareaSub(request,id):
    tareasub = get_object_or_404(TareaSub,id=id)
    tareasub.delete()
    return redirect(to="ListarTareaSub")

#Comienzo Atraso
def AgregarAtraso(request):
    data = {
        'form': AtrasoForm()
    }
    if request.method == 'POST':
        formulario = AtrasoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data["form"] = formulario
    return render(request,'Atraso/agregar.html', data)

def ListarAtraso(request):
    Atrasos = Atraso.objects.all()
    data = {
        'Atrasos': Atrasos
    }
    return render(request, 'Atraso/listar.html', data)

def ModificarAtraso(request, id):
    atraso = get_object_or_404 (Atraso,id=id)
    data = {
        'form': AtrasoForm(instance=atraso)
    }

    if request.method == 'POST':
        formulario = AtrasoForm(data=request.POST, instance=atraso)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="ListarAtraso")
        data["form"] = formulario

    return render(request, 'Atraso/modificar.html', data)

def EliminarAtraso(request,id):
    atraso = get_object_or_404(Atraso,id=id)
    atraso.delete()
    return redirect(to="ListarAtraso")

#Comienzo Problema
def AgregarProblema(request):
    data = {
        'form': ProblemaForm()
    }
    if request.method == 'POST':
        formulario = ProblemaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data["form"] = formulario
    return render(request,'Problema/agregar.html', data)

def ListarProblema(request):
    Problemas = Problema.objects.all()
    data = {
        'Problemas': Problemas
    }
    return render(request, 'Problema/listar.html', data)

def ModificarProblema(request, id):
    problema = get_object_or_404 (Problema,id=id)
    data = {
        'form': ProblemaForm(instance=problema)
    }

    if request.method == 'POST':
        formulario = ProblemaForm(data=request.POST, instance=problema)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="ListarProblema")
        data["form"] = formulario

    return render(request, 'Problema/modificar.html', data)

def EliminarProblema(request,id):
    problema = get_object_or_404(Problema,id=id)
    problema.delete()
    return redirect(to="ListarProblema")
