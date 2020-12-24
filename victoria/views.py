from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from .models import Reserva
from .forms import CheckReservationForm
#
from django.utils import timezone
import datetime as dt


def index(request):
    return render(request, 'victoria/index.html')


def reservas(request):
    reservas = Reserva.objects.all()
    context = {'reservas': reservas}
    return render(request, 'victoria/reservas.html', context)


def availability(request):
    form = CheckReservationForm(request.POST or None)
    if request.method == 'POST':
        print('datos del post:', request.POST)

        if form.is_valid():
            cd = form.cleaned_data.get('date')
            reservas = Reserva.objects.filter(date=cd)
            print('reservas:', reservas)
            print(type(reservas))
            form = CheckReservationForm()
            context = {
                'reservas': reservas,
                'form': form
            }
            return render(request, 'victoria/daylist.html', context)
    else:
        print('errores del form: ', form.errors)

    return render(request, 'victoria/res_form.html', {'form': form})


def prueba(request):
    reservas = Reserva.objects.filter(date=request.POST['date'])
    context = {
        'reservas': reservas,
    }

    return render(request, 'victoria/availability.html', context)
