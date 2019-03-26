from django.shortcuts import render
from django.http import HttpResponse

from osoby.models import Absolwent

def index(request):
    return HttpResponse("<h1>Witaj w Django!</h1>")

def test(request):
    return HttpResponse("To tylko test")

def lista_osob(request):
    osoba = Absolwent.objects.all()
    kontekst = {'osoby': osoba}
    return render(request, 'osoby/lista_osob.html', kontekst)