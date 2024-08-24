from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from .forms import UsuarioForm

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/usuarios.html', {'usuarios': usuarios})

def create_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listagem_usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/create_usuario.html', {'form': form})

def update_usuario(request, id):
    usuario = get_object_or_404(Usuario, id_usuario=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listagem_usuarios')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/update_usuario.html', {'form': form})

def delete_usuario(request, id):
    usuario = get_object_or_404(Usuario, id_usuario=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listagem_usuarios')
    return render(request, 'usuarios/delete_usuario.html', {'usuario': usuario})
