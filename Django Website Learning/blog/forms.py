from django import forms
from django.db import models

from .models import BlogPost

class BlogpostForm(forms.ModelForm):
    class Meta: 
        model = BlogPost
        fields = [
            'blogTitle', 
            'blogText',
        ]

        widget = {
            'blogTitle': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 50,}),
            'blogText': forms.TextInput(attrs={'class': 'form-control'})
        } 