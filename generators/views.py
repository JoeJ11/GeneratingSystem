from django.shortcuts import render
import json
from django.http import HttpResponse


# Create your views here.

def index(request):
	return HttpResponse("You're at the index page.")

def load(request):
	return HttpResponse("load")