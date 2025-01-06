from .models import *
from django import forms


class newpostform(forms.ModelForm) :
    class Meta :
        model = Post
        fields = ('label', 'caption', 'status')