from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.


def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.Post:
        username = request.Post.get('username')
        password = request.Post.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
             login(request, usuario)
             return redirect('/')
        else:
            messages.error(request, "Usuário ou Senha Inválida")
    return redirect('/')


@login_required(login_url='/login/')

def lista_eventos(request):
   usuario = request.user
   evento = Evento.objects.filter(usuario=usuario)
   #evento = Evento.objects.all()#com o get(id=1)eu listo só 1
   dados = {'eventos': evento}
   return render(request, 'agenda.html', dados)

