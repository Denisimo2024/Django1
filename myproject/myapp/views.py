from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Главная страница</h1>")

def data_view(request):
    return HttpResponse("<h1>Это страница Data</h1>")

def test_view(request):
    return HttpResponse("<h1>Это страница Test</h1>")
