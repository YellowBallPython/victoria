from django.contrib import admin
from .models import Reserva

@admin.register(Reserva)
class ReservaUser(admin.ModelAdmin):
    list_display = ('owner', 'date', 'check_in', 'check_out', 'up_to_date')
    list_filter =  ('owner', 'date')
    ordering = ('-date', 'up_to_date')
