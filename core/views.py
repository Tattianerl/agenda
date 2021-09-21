from django.shortcuts import render #redirect
from core.models import Evento



# Create your views here.

def lista_eventos(request):

   #evento = Evento.objects.filter(usuario=usuario)
   evento = Evento.objects.all()#com o get(id=1)eu listo só 1
   dados = {'eventos': evento}
   return render(request, 'agenda.html', dados)

