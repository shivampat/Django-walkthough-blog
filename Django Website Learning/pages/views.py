from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    myDict = {
        'myName': 'Shivam',
        'myAge': '19',
        'theYear': '2023',
    }
    return render(request, 'home.html', myDict)

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})

def about_view(request, *args, **kwargs):
    return render(request, 'about.html', {})