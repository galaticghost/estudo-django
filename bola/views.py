from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from bola.forms import UserForm
from bola.models import User

def index(request):
    template = loader.get_template('bola/base.html')
    return HttpResponse(template.render(request=request))

def ohboy(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            username = form['username'].value()
            password = form['password'].value()
            us = User(username=username,password=password)
            us.set_password(us.password)
            us.save()
    form = UserForm()
    return render(request,template_name=('bola/ohboy.html'),context={'form':form})