from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from  django.urls import reverse

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
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            nazwa = form.cleaned_data['nazwa']
            haslo = form.cleaned_data['haslo']
            user = authenticate(request, username=nazwa, password=haslo)
            if user is not None:
                login(request, user)
                messages.success(request, "Zostałeś zalogowany!")
                return redirect(reverse('osoby:osoby'))
            else:
                messages.error(request, "Błedny login lub hasło!")
    else:
        form = UserLoginForm()
    kontekst = {'form' : form}
    return render(request, 'osoby/loguj_osobe.html', kontekst)


def wyloguj_osobe(request):
    logout(request)
    messages.success(request, "Zostałeś wylogowany!")
    return redirect(reverse('osoby:osoby'))