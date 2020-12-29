from django import forms
from .models import Reserva
import datetime


class CheckReservationForm(forms.Form):
    date = forms.DateField(label="Date", initial=datetime.date.today, widget=forms.SelectDateWidget)

class MakeReservationForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['date', 'check_in', 'check_out']