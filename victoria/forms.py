from django import forms


class CheckReservationForm(forms.Form):
    date = forms.DateField(label="Date")
