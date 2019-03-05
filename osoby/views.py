from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Witaj Django!</h1>")
