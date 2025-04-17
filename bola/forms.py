from django import forms
from django.forms import ModelForm
from bola.models import User

class XinaForm(forms.Form):
    nome = forms.CharField(label='Su nombre',max_length=100)

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username","password"]