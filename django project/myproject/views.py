from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'website Kematian',
        'heading': 'Selamat Datang Di Website Kematian',
        'subheading': 'INI WEBSITE KEMATIAN'
    }
    return render(request, 'index.html', context)

