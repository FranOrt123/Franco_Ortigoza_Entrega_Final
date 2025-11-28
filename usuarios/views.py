from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from usuarios.forms import FormularioRegistro

def iniciar_sesion(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request, usuario)
            return redirect("inicio")
    else: 
         formulario = AuthenticationForm()
    return render(request, 'iniciar_sesion.html', {"formulario": formulario})

def registro(request):
    if request.method == "POST":
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            
          formulario.save()  

        return redirect("iniciar_sesion")
    else: 
        formulario = FormularioRegistro()
    return render(request, 'registro.html', {"formulario": formulario})


@login_required()
def perfil_usuario(request):
    usuario = request.user
    return render(request, 'perfil.html', {'usuario': usuario})