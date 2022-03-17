from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("Tech with James!")

def v1(response):
    return HttpResponse("view 1")

def main(response):
    return HttpResponse("main")