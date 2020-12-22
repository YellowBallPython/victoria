from django.shortcuts import render
from .models import Reserva
#
from django.utils import timezone
import datetime as dt



def index(request):
    return render(request, 'victoria/index.html')


def reservas(request):
    reservas = Reserva.objects.all()
    context = {'reservas': reservas}
    return render(request, 'victoria/reservas.html', context)


def res_form(request):
    return render(request, 'victoria/res_form.html')

def prueba(request):
    reservas = Reserva.objects.filter(date=request.POST['date'])
    context = {
        'reservas':reservas,
    }

    return render(request, 'victoria/prueba.html', context)

