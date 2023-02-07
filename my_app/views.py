from django.shortcuts import render
from .forms import SearchForm
from bs4 import BeautifulSoup
import requests
import re

# Create your views here.

def getHTML(link):
    response = requests.get(link)
    print("scraping HTML......")
    # print(response.text.pre)
    doc = BeautifulSoup(response.text, "html.parser" )
    print(doc.prettify())
    return doc

# getHTML("https://www.jumia.com.ng/catalog/?q=tecno+camon+19")
# jumia_search = "https://www.jumia.com.ng/catalog/?q=tecno+camon+19"


def home(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data.get('search_field')
            data = data.replace(' ', '+')
            jumia_search = "https://www.jumia.com.ng/catalog/?q="
            rdata = jumia_search + data
            # print(rdata)
            # print(data)
            getHTML(rdata)
    else:
        form = SearchForm()        
    return render(request, 'my_app/home.html', {'form': form})


