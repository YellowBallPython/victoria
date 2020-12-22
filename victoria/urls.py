from django.urls import path
from victoria import views as victoria_views


app_name = 'victoria'
urlpatterns = [
    path('', victoria_views.index, name="index"),
    path('reservas/', victoria_views.reservas, name='reservas'),
    path('reservas/create', victoria_views.res_form, name='res_form'),
    path('reservas/prueba', victoria_views.prueba, name='prueba'),
]
