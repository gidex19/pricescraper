from django.shortcuts import render, redirect
from .forms import SearchForm
from bs4 import BeautifulSoup
import requests
import re
import json

# Create your views here.

def getHTMLkonga(link):
    response = requests.get(link)
    # print("scraping Konga HTML......")
    # print(response.text.pre)
    soup = BeautifulSoup(response.text, "html.parser" )
    # print(doc.prettify())
    # print(response.text)
    # print("print out...")
    content = soup.find('script', {"id": "__NEXT_DATA__"}).string
    dictionary = json.loads(content) 
    check = dictionary["props"]["initialProps"]["pageProps"]["resultsState"]["content"]["hits"]
    data_dict = {}
    check = check[:4]
    for index, item  in enumerate(check):
        sub_dict = {}
        sub_dict["product_name"] = item['name']
        sub_dict["product_price"] = item['price']
        sub_dict["image_url"] = "https://www-konga-com-res.cloudinary.com/w_auto,f_auto,fl_lossy,dpr_auto,q_auto/media/catalog/product" + item['image_thumbnail_path']
        sub_dict["product_url"] = "https://www.konga.com/product/" + item['url_key']
        sub_dict["rating"] = item['rating']
        data_dict[index] = sub_dict
    # print(data_dict)
    # for i in data_dict:
    #     print("=====================")
    #     print(data_dict[i])
    #     print("=====================")
    return data_dict
    # print(check)
    # return soup.find('script', {"id": "__NEXT_DATA__"}).finc
    # return soup.prettify("utf-8")

def getHTMLjumia(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    # print("printing all script tags")
    article_tags = soup.find_all('article', {"class": "c-prd"})[:4]
    # print(scripts_tags[3].string)
    data_dict = {}
    for index, item in enumerate(article_tags):
        sub_dict = {}
        # print("--------------------------------------------")
        product_url = "https://www.jumia.com.ng" + item.findChild("a", {"class": "core"}).get("href")
        image_url = item.findChild("div", {"class", "img-c"}).findChild("img", {"class": "img"}).get("data-src") 
        product_name = item.findChild("div", {"class", "info"}).findChild("h3", {"class": "name"}).text 
        product_price = item.findChild("div", {"class", "info"}).findChild("div", {"class": "prc"}).text
        # old_price = item.findChild("div", {"class", "info"}).findChild("div", {"class": "s-prc-w"}).findChild("div", {"class": "old"}).text


        sub_dict['product_name'] = product_name 
        sub_dict['product_price'] = product_price 
        sub_dict['image_url'] = image_url 
        sub_dict['product_url'] = product_url 
        data_dict[index] = sub_dict
    for i in data_dict:
        print("=====================")
        print(data_dict[i])
        print("=====================")
    return data_dict
    # print(soup.text)
    # return soup.text
    # return soup.prettify("utf-8")
    return data_dict

# getHTML("https://www.jumia.com.ng/catalog/?q=tecno+camon+19")
# jumia_search = "https://www.jumia.com.ng/catalog/?q=tecno+camon+19"
# https://www.konga.com/search?search=redmi%20note%2010

def home(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data.get('search_field')
            return redirect('results', key= data)
            
            
            
            # return redirect('')
            
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

def results(request, key):
    data  = key
    jumia_search_string = data.replace(' ', '+')
    konga_search_string = data.replace(' ', '%20')
    jumia_url = "https://www.jumia.com.ng/catalog/?q="
    konga_url = "https://www.konga.com/search?search="
    jumia_purl = jumia_url + jumia_search_string 
    konga_purl = konga_url + konga_search_string
    jumia_data = getHTMLjumia(jumia_purl)
    konga_data = getHTMLkonga(konga_purl)
    context = {'jumia_data': jumia_data, 'konga_data': konga_data}
    print(key)
    print(jumia_data)
    print(konga_data)
    return render(request, 'my_app/results.html', context)
