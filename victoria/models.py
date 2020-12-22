from django.db import models
from django.contrib.auth.models import User


class Reserva(models.Model):

    STATUS_CHOICES = [

    ]

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
