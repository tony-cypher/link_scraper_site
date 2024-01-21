from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Link
import requests
from bs4 import BeautifulSoup

# Create your views here.

def scrape(request):
    if request.method == 'POST':
        site = request.POST.get('site', '')
        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')

        x = 0
        for link in soup.find_all('a'):
            x +=1
            link_address = link.get('href')
            link_text = link.string
            Link.objects.create(no=x,address=link_address, name=link_text)
        return HttpResponseRedirect('/')
    else:
        data = Link.objects.all()
    
    return render(request, 'scraper/result.html', {'data':data})

def clear(request):
    Link.objects.all().delete()
    return render(request, 'scraper/result.html')