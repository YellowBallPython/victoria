from django.urls import path
from victoria import views as victoria_views


app_name = 'victoria'
urlpatterns = [
    path('', victoria_views.index, name="index"),
    path('reservas/', victoria_views.reservas, name='reservas'),
    path('reservas/availability/', victoria_views.availability, name='availability'),
    path('reservas/make', victoria_views.make_reservation, name='make'),
]
