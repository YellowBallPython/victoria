from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


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
        return f'Dueñ@: {self.owner}'

    def get_absolute_url(self):
        return reverse('victoria:availability',
                       args=[self.date])

    def get_reservations_by_date(self, input_date):
        dates = Reserva.objects.filter(
            date__year=input_date.year).filter(
                date__month=input_date.month).filter(
                    date__day=input_date.day
        )
        return dates
