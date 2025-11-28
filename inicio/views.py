from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from inicio.models import Camiseta
from inicio.forms import CrearCamisetas, BuscarCamisetas
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, "inicio.html")

def otra(request):
    return render(request, "otra.html")

@login_required
def crear_camiseta(request):
    if request.method == "POST":
        formulario = CrearCamisetas(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
        
            camiseta = Camiseta(club=info.get("club"), modelo=info.get("modelo"), talle=info.get("talle"))
            camiseta.save()

            return redirect("listado")
    else:
        formulario = CrearCamisetas()

    return render(request, "crear_camiseta.html", {'formulario': formulario})

def listar_camisetas(request):

    formulario = BuscarCamisetas(request.GET)
    camisetas = Camiseta.objects.all()

    if formulario.is_valid():
        club_buscado = formulario.cleaned_data.get("club")
        if club_buscado:
            camisetas = Camiseta.objects.filter(club__icontains=club_buscado)

    return render(request, "listar_camisetas.html", {'camisetas': camisetas, 'formulario': formulario})


def ver_camiseta(request, id):
    camiseta = get_object_or_404(Camiseta, id=id)
    return render(request, "ver_camiseta.html", {'camiseta': camiseta})


class EditarCamisetas(LoginRequiredMixin, UpdateView):
    model = Camiseta
    template_name = "editar_camiseta.html"
    fields = ['club', 'modelo', 'talle']        
    success_url = reverse_lazy('listado')

class EliminarCamisetas(LoginRequiredMixin, DeleteView):
    model = Camiseta
    template_name = "eliminar_camiseta.html"
    success_url = reverse_lazy('listado')
    