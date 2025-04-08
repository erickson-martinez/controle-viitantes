from django.shortcuts import render

from django.http import HttpResponse
from django.views import View
def index(request):
    return HttpResponse("Olá, mundo! Agora em Django!")
