from django import forms

class XinaForm(forms.Form):
    nome = forms.CharField(label='Su nombre',max_length=100)