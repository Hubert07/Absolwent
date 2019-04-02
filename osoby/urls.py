from django.urls import path

from . import views

app_name='osoby'
urlpatterns = [
    path('', views.lista_osob, name='osoby'),
    path('loguj/', views.loguj_osobe, name='loguj_osobe'),
    path('wyloguj/', views.wyloguj_osobe, name='wyloguj_osobe'),
]