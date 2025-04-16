from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('bola/base.html')
    return HttpResponse(template.render(request=request))

def ohboy(request):
    response = redirect(index)
    return response