from django import forms
from django.forms import ModelForm
from bola.models import Community

class CommunityForm(ModelForm):
    class Meta:
        model = Community
        fields = ('nome','sobre')
        widgets = {
            'sobre': forms.Textarea(),
        }