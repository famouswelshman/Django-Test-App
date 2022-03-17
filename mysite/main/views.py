from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("Tech with James!")

def v1(response):
    retunr HttpResponse("<h1>view 1</h1>")