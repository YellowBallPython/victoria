from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
import datetime
from .models import Reserva
from .forms import CheckReservationForm, MakeReservationForm
from django.contrib.auth.admin import User


def index(request):
    return render(request, 'victoria/index.html')


def reservas(request):
    reservas = Reserva.objects.all()
    context = {'reservas': reservas}
    return render(request, 'victoria/reservas.html', context)


def availability(request):
    form = CheckReservationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data.get('date')
            reservas = Reserva.objects.filter(date=cd)
            form = CheckReservationForm()
            context = {
                'reservas': reservas,
                'form': form
            }
            return render(request, 'victoria/daylist.html', context)
    return render(request, 'victoria/res_form.html', {'form': form})


def prueba(request):
    reservas = Reserva.objects.filter(date=request.POST['date'])
    context = {
        'reservas': reservas,
    }

    return render(request, 'victoria/availability.html', context)

def make_reservation(request):

    apertura = datetime.time(hour=9, second=0, microsecond=0)
    cierre = datetime.time(hour=21, second=0, microsecond=0)

    form = MakeReservationForm(request.POST or None) #It's a modelForm
    if request.method == 'POST':
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            cd_ci = cd.get('check_in')
            cd_co = cd.get('check_out')
            cd_date = cd.get('date')
            owner = User.objects.get(pk=1)
            if cd_ci > apertura and cd_co < cierre:
                reservas = Reserva.objects.filter(date=cd_date)
                Reserva(owner=owner, date=cd_date, check_out=apertura)
                Reserva(owner=owner, date=cd_date, check_in=cierre)
                for i in range(len(reservas)):
                    if reservas[i].check_out < cd_ci and reservas[i + 1].check_in > cd_co:
                        new_res = Reserva(owner=owner, date=cd_date, check_in=cd_ci, check_out=cd_co)
                        new_res.save()
                        context = {
                            'new_res': new_res,
                        }
                        return render(request, 'victoria/completed.html', context)
    else:
        return render(request, 'victoria/make.html', {'form': form})