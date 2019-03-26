from django.shortcuts import render
from django.http import HttpResponse

from osoby.models import Absolwent
from osoby.forms import UserLoginForm


def index(request):
    return HttpResponse("<h1>Witaj w Django!</h1>")


def test(request):
    return HttpResponse("To tylko test")


def lista_osob(request):
    osoba = Absolwent.objects.all()
    kontekst = {'osoby': osoba}
    return render(request, 'osoby/lista_osob2.html', kontekst)


def loguj_osobe(request):
    form = UserLoginForm()
    kontekst = {'form' : form}
    return render(request, 'osoby/loguj_osobe.html', kontekst)