from django.shortcuts import render
from .forms import SearchForm
from bs4 import BeautifulSoup
import requests
import re
import json

# Create your views here.

def getHTMLkonga(link):
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
        print(item['image_thumbnail_path'])
        print("===============================================================")
        print("      ")
    # print(check)
    return soup.find('script', {"id": "__NEXT_DATA__"}).finc
    # return soup.prettify("utf-8")

def getHTMLjumia(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    # print("printing all script tags")
    article_tags = soup.find_all('article', {"class": "c-prd"})[:10]
    # print(scripts_tags[3].string)
    for item in article_tags:
        print("--------------------------------------------")
        url = "https://www.jumia.com.ng" + item.findChild("a", {"class": "core"}).get("href")
        image_url = item.findChild("div", {"class", "img-c"}).findChild("img", {"class": "img"}).get("data-src") 
        product_name = item.findChild("div", {"class", "info"}).findChild("h3", {"class": "name"}).text 
        product_price = item.findChild("div", {"class", "info"}).findChild("div", {"class": "prc"}).text
        # old_price = item.findChild("div", {"class", "info"}).findChild("div", {"class": "s-prc-w"}).findChild("div", {"class": "old"}).text

        print(url)
        print(image_url)
        print(product_name)
        print(product_price)
        print("--------------------------------------------")
    print(len(article_tags))
    # print(soup.text)
    # return soup.text
    return soup.prettify("utf-8")


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
            j = getHTMLjumia(jumia_purl)
            # k = getHTMLkonga(konga_purl)
            print("form submitted")
            getHTMLjumia(jumia_purl)
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


