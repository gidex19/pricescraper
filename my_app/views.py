from django.shortcuts import render
from .forms import SearchForm
from bs4 import BeautifulSoup
import requests
import re
import json

# Create your views here.

def getHTML(link):
    response = requests.get(link)
    print("scraping HTML......")
    # print(response.text.pre)
    soup = BeautifulSoup(response.text, "html.parser" )
    # print(doc.prettify())
    # print(response.text)
    print("print out...")
    content = soup.find('script', {"id": "__NEXT_DATA__"}).string
    dictionary = json.loads(content) 
    check = dictionary["props"]["initialProps"]["pageProps"]["resultsState"]["content"]["hits"]
    for item in check:
        print("===============================================================")
        print(item['name'])
        print(item['price'])
        print(item['product_type'])
        print(item['url_key'])
        print(item['price'])
        print(item['description'])
        print(item['rating'])
        print("===============================================================")
        print("     ")
    # print(check)
    return soup.find('script', {"id": "__NEXT_DATA__"})
    # return soup.prettify("utf-8")




# getHTML("https://www.jumia.com.ng/catalog/?q=tecno+camon+19")
# jumia_search = "https://www.jumia.com.ng/catalog/?q=tecno+camon+19"
# https://www.konga.com/search?search=redmi%20note%2010

def home(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data.get('search_field')
            jumia_search_string = data.replace(' ', '+')
            konga_search_string = data.replace(' ', '%20')
            jumia_url = "https://www.jumia.com.ng/catalog/?q="
            konga_url = "https://www.konga.com/search?search="
            jumia_purl = jumia_url + jumia_search_string
            konga_purl = konga_url + konga_search_string
            # print(rdata)
            # print(data)
            # j = getHTML(jumia_purl)
            k = getHTML(konga_purl)
            print("form submitted")
            # print(k)
            # with open('konga.html', 'wb') as f:
            #     f.write(k)
            #     f.close()
            #     print("konga file saved")
            # with open('jumia.html', 'wb') as f:
            #     f.write(j)
            #     f.close()    
            #     print("jumia file saved")
    else:
        form = SearchForm()        
    return render(request, 'my_app/home.html', {'form': form})


