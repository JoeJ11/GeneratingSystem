from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def register(request):
    return HttpResponse("Register")

def message(request, id):
    return HttpResponse("Message with ID {}".format(id))

def delete(request, id):
    return HttpResponse("Delete with ID {}".format(id))
