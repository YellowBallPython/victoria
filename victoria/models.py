from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import datetime as dt


class Reserva(models.Model):

    date = models.DateField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    up_to_date = models.BooleanField(
        default=True, verbose_name='Próximas fechas')

    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='reservation')

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return f'Dueño: {self.owner}'

    def get_absolute_url(self):
        return reverse('victoria:availability',
                       args=[self.date])

    def get_reservations_by_date(self, input_date):
        dates = Reserva.objects.filter(date=input_date)
        return dates

    def make_res(self, reserva):
        if not reserva:
            return 2
        else:
            date = reserva.date
            apertura = dt.time(9, 0, 0)
            cierre = dt.time(21, 0, 0)
            midnight = dt.time(0, 0)
            user_prop = User.objects.get(pk=1)

            today_res = [i for i in Reserva.objects.filter(date=date)]
            r1 = Reserva(owner=user_prop, check_in=midnight,
                         check_out=apertura, date=date)
            r2 = Reserva(owner=user_prop, check_in=cierre,
                         check_out=midnight, date=date)
            today_res.insert(0, r1)
            today_res.append(r2)

            for todayRes in today_res:
                index = today_res.index(todayRes)
                elif reserva.check_in > todayRes.check_out and reserva.check_out < today_res[(index) + 1].check_in:
                    reserva.save()
                else:
                    pass
            try:
                check_res = Reserva.objects.get(id=reserva.id)
                return 0
            except self.model.DoesNotExist:
                return 1
