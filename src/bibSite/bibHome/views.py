from django.shortcuts import render
from .models import Bib
# Create your views here.

bibs = [
    {
        'title': "Machine Learning",
        'author': 'Rohan',
        'bib': 'coming soon',
        'date_searched': 'March 28, 2020'
    },
    {
        'title': "RBFT",
        'author': 'S',
        'bib': 'coming soon',
        'date_searched': 'March 28, 2020'
    }
]

def home(request):
    context = {
        'bibs': Bib.objects.all()
    }
    return render(request, 'bibHome/home.html', context)

def about(request):
    return render(request, 'bibHome/about.html', {'title': 'About' })