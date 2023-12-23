from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib import messages
from django.views.decorators.http import require_GET
from accounts.views import *
from django.core.exceptions import ObjectDoesNotExist


def user_login(request):  
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            try:
                user_profile = user.userprofile
            except ObjectDoesNotExist:                
                User_profile.objects.create(user=user)
            return redirect('Proyecto:inicio')
        else:
            return render(request, 'Proyecto/login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'Proyecto/login.html')



def registro(request):    
    if request.method == 'POST':   
        form = UserCreationForm(request.POST)     
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('Proyecto:inicio')
        else:
            messages.error(request, 'Error en el formulario. Por favor, corrige los errores.')
    else:
        form = UserCreationForm()

    return render(request, 'Proyecto/registro.html', {"form": form})
    


@require_GET
def user_logout(request):
    logout(request)
    return redirect('Proyecto:inicio')

@login_required
def perfil(request):
    try:
        user_profile = request.user.userprofile
    except User_profile.DoesNotExist:        
        user_profile = None

    return render(request, 'Proyecto/perfil.html', {'user_profile': user_profile})
    


@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method=='POST':
        mi_formulario = UserEditForm(request.POST, instance= request.user)

        if mi_formulario.is_valid():
            mi_formulario.save()
            return render (request, 'Proyecto/index.html')

    

@login_required
def eliminar_perfil(request):
    perfil = User_profile.objects.get(user=request.user)
    if request.method=="POST":
        perfil.delete()
        return redirect ('Proyecto:inicio')
    
    return render (request,'Proyecto/eliminar_perfil.html', {"perfil": perfil})
