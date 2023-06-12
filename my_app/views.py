import random, time
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import SearchForm, LoginForm, SignUpForm
from .models import Customuser, SavedProduct
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from bs4 import BeautifulSoup
from django.contrib.auth.hashers import *
from django.contrib.auth.decorators import login_required
from scrapingbee import ScrapingBeeClient
import requests
# from msedge.selenium_tools import EdgeOptions
# from msedge.selenium_tools import Edge

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
import json



# payload = {'api_key': '647db17e4b69347cd45bbbd7', 'url': 'https://www.jumia.com.ng/catalog/?q=elepaq+generator', 'dynamic':'false'}
# resp = requests.get('https://api.scrapingdog.com/scrape', params=payload)
# print("----------------------------------------------")
# print (resp.text)
# print("----------------------------------------------")



# Create your views here.



proxy = '103.69.108.78'
user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 OPR/94.0.0.0 (Edition Yx GX)',
    'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/111.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Tangled/1.22.3',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Whale/3.19.166.16 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36/qvIf4R6rTa',

]
proxies = {"http": proxy, "https": proxy}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}

validproxies = ['3.226.79.79:80', '20.241.236.196:3128', '20.241.236.196:3128', '20.241.236.196:3128', '186.121.235.66:8080', '128.14.140.2:11772', '128.14.140.2:11772', '20.241.236.196:3128', '51.159.0.236:3128', '51.159.0.236:3128']
newproxies = []
ppr = {"http": "http://3.226.79.79:80", "https": "http://20.241.236.196:3128", "https": "http://186.121.235.66:8080", "https": "http://128.14.140.2:11772"}
new_ppr = {"http": "http://197.253.40.162:80", "https": "http://105.112.130.186:8080"}

user_agent = random.choice(user_agent_list)
# print(user_agent)


def scrapingBeefunc(link):
    client = ScrapingBeeClient(api_key='BNJ7W1VCKRLUIIJL9DDFM5GQWJ6OU4ZWZOVP2TWAUNDO2W9WB6XWZQ1FWE1T91RX2ZV9JC231Z2N2QFW')
    response = client.get(link)
    return response.text

def getHTMLjumia(link):
    # user_agent = random.choice(user_agent_list)
    response_text = requests.get(link, headers={'User-Agent': user_agent}).text

    # payload = {'api_key': '647db17e4b69347cd45bbbd7', 'url': link, 'dynamic':'false'}
    # response = requests.get('https://api.scrapingdog.com/scrape', params=payload)

    # client = ScrapingBeeClient(api_key='PPC6P70AHM5GYZGZ15H1C3S1S1NFY6E7V1E1QUZ1AAOZ2UM1PK8CFPD0RX2HZH2YAMBCKJBL7EMUPNJ5')
    # response = client.get(link)

    # response_text = scrapingBeefunc(link)
    
    soup = BeautifulSoup(response_text, "html.parser")
    # soup = BeautifulSoup(response.text, "html.parser")
    # print("printing all script tags")
    article_tags = soup.find_all('article', {"class": "c-prd"})[:2]
    # print(scripts_tags[3].string)
    data_dict = {}
    for index, item in enumerate(article_tags):
        sub_dict = {}
        # print("--------------------------------------------")
        product_url = "https://www.jumia.com.ng" + \
            item.findChild("a", {"class": "core"}).get("href")
        product_id = item.findChild("a", {"class": "core"}).get("data-id")
        image_url = item.findChild(
            "div", {"class", "img-c"}).findChild("img", {"class": "img"}).get("data-src")
        product_name = item.findChild("div", {"class", "info"}).findChild(
            "h3", {"class": "name"}).text
        product_price = item.findChild("div", {"class", "info"}).findChild(
            "div", {"class": "prc"}).text
        # old_price = item.findChild("div", {"class", "info"}).findChild("div", {"class": "s-prc-w"}).findChild("div", {"class": "old"}).text
        # print(product_id)
        sub_dict["product_id"] = product_id
        sub_dict['product_name'] = product_name
        sub_dict['product_price'] = product_price
        sub_dict['image_url'] = image_url
        sub_dict['product_url'] = product_url
        sub_dict['product_store'] = 'Jumia'
        data_dict[index] = sub_dict

    return data_dict


def getHTMLkonga(link):
    response_text = requests.get(link).text
    # print("scraping Konga HTML......")
    # print(response.text.pre)

    # payload = {'api_key': '647db17e4b69347cd45bbbd7', 'url': link, 'dynamic':'false'}
    # response = requests.get('https://api.scrapingdog.com/scrape', params=payload)

    # client = ScrapingBeeClient(api_key='PPC6P70AHM5GYZGZ15H1C3S1S1NFY6E7V1E1QUZ1AAOZ2UM1PK8CFPD0RX2HZH2YAMBCKJBL7EMUPNJ5')
    # response = client.get(link)

    response_text = scrapingBeefunc(link)
    # soup = BeautifulSoup(response.text, "html.parser")
    # print(doc.prettify())
    # print(response.text)
    # print("print out...")
    soup = BeautifulSoup(response_text, "html.parser")
    content = soup.find('script', {"id": "__NEXT_DATA__"}).string
    dictionary = json.loads(content)
    check = dictionary["props"]["initialProps"]["pageProps"]["resultsState"]["content"]["hits"]
    data_dict = {}
    check = check[:2]
    for index, item in enumerate(check):
        sub_dict = {}
        sub_dict["product_id"] = item['sku']
        sub_dict["product_name"] = item['name']
        sub_dict["product_price"] = item['price']
        sub_dict["image_url"] = "https://www-konga-com-res.cloudinary.com/w_auto,f_auto,fl_lossy,dpr_auto,q_auto/media/catalog/product" + \
            item['image_thumbnail_path']
        sub_dict["product_url"] = "https://www.konga.com/product/" + \
            item['url_key']
        sub_dict["rating"] = item['rating']
        sub_dict['product_store'] = 'Konga'
        data_dict[index] = sub_dict
   
    return data_dict
    


def getHTMLkara(link):
    response_text = requests.get(link, headers={'User-Agent': user_agent}, ).text
    # soup = BeautifulSoup(response.text, "html.parser")

    # payload = {'api_key': '647db17e4b69347cd45bbbd7', 'url': link, 'dynamic':'false'}
    # response = requests.get('https://api.scrapingdog.com/scrape', params=payload)

    # client = ScrapingBeeClient(api_key='PPC6P70AHM5GYZGZ15H1C3S1S1NFY6E7V1E1QUZ1AAOZ2UM1PK8CFPD0RX2HZH2YAMBCKJBL7EMUPNJ5')
    # response = client.get(link)
    

    # response_text = scrapingBeefunc(link)
    soup = BeautifulSoup(response_text, "html.parser")
    li_tags = soup.find_all('li', {"class": "item product product-item"})[:2]
    data_dict = {}
    for index, item in enumerate(li_tags):
        sub_dict = {}
        product_id = item.findChild(
            "div", {"class", "price-final_price"}).get("data-product-id").strip()
        product_name = item.findChild(
            "a", {"class", "product-item-link"}).text[1:]
        product_url = item.findChild(
            "a", {"class", "product-item-link"}).get("href")
        image_url = item.findChild(
            "img", {"class", "product-image-photo"}).get("data-original")
        product_price = item.findChild("span", {"class", "price-wrapper"}).text
        product_price = product_price[4:-3]

        sub_dict["product_id"] = product_id
        sub_dict['product_name'] = product_name
        sub_dict['product_price'] = product_price
        sub_dict['image_url'] = image_url
        sub_dict['product_url'] = product_url
        sub_dict['product_store'] = 'Kara'
        data_dict[index] = sub_dict

    return data_dict
    


def getHTMLkaiglo(link, headers={'User-Agent': user_agent},):
    response_text = requests.get(link).text
    # soup = BeautifulSoup(response.text, "html.parser")

    # payload = {'api_key': '647db17e4b69347cd45bbbd7', 'url': link, 'dynamic':'false'}
    # response = requests.get('https://api.scrapingdog.com/scrape', params=payload)

    # client = ScrapingBeeClient(api_key='PPC6P70AHM5GYZGZ15H1C3S1S1NFY6E7V1E1QUZ1AAOZ2UM1PK8CFPD0RX2HZH2YAMBCKJBL7EMUPNJ5')
    # response = client.get(link)
    
    # response_text = scrapingBeefunc(link)
    soup = BeautifulSoup(response_text, "html.parser")

    li_tags = soup.find_all('li', {"class": "item product product-item"})[:2]
    data_dict = {}
    for index, item in enumerate(li_tags):
        sub_dict = {}
        product_id = item.findChild(
            "div", {"class", "price-final_price"}).get("data-product-id").strip()
        product_name = item.findChild(
            "a", {"class", "product-item-link"}).text[1:]
        product_url = item.findChild(
            "a", {"class", "product-item-link"}).get("href")
        image_url = item.findChild(
            "img", {"class", "product-image-photo"}).get("data-original")
        product_price = item.findChild("span", {"class", "price-wrapper"}).text
        product_price = product_price[4:-3]

        sub_dict["product_id"] = product_id
        sub_dict['product_name'] = product_name
        sub_dict['product_price'] = product_price
        sub_dict['image_url'] = image_url
        sub_dict['product_url'] = product_url
        sub_dict['product_store'] = 'Kara'
        data_dict[index] = sub_dict

    return data_dict

def getHTMLslot(link):
    response_text = requests.get(link, headers={'User-Agent': user_agent}, ).text
    # soup = BeautifulSoup(response.text, "html.parser")

    # payload = {'api_key': '647db17e4b69347cd45bbbd7', 'url': link, 'dynamic':'false'}
    # response = requests.get('https://api.scrapingdog.com/scrape', params=payload)

    # client = ScrapingBeeClient(api_key='PPC6P70AHM5GYZGZ15H1C3S1S1NFY6E7V1E1QUZ1AAOZ2UM1PK8CFPD0RX2HZH2YAMBCKJBL7EMUPNJ5')
    # response = client.get(link)
    

    # response_text = scrapingBeefunc(link)
    soup = BeautifulSoup(response_text, "html.parser")
    product_holders = soup.findChildren('div', {"class": "item-product"})[:2]
    data_dict = {}
    for index, item in enumerate(product_holders):
        sub_dict = {}
        product_id = "slot" + item.findChild("a", {"class": "quickview-link"}).get("data-id")
        product_name = item.findChild("img", {"class": "product-image-photo"}).get("alt")
        product_url = item.findChild("a", {"class": "product-thumb-link"}).get("href")
        image_url = item.findChild("img", {"class": "product-image-photo"}).get("src")
        product_price = item.findChild("span", {"class": "price"}).text
        # product_price = product_price[4:-3]

        sub_dict["product_id"] = product_id
        sub_dict['product_name'] = product_name
        sub_dict['product_price'] = product_price
        sub_dict['image_url'] = image_url
        sub_dict['product_url'] = product_url
        sub_dict['product_store'] = 'Slot Ng'
        data_dict[index] = sub_dict

    return data_dict



def home(request):
    url = 'https://slot.ng/catalogsearch/result/?q=infinix'

    jumia_response = requests.get('https://www.jumia.com.ng')
    konga_response = requests.get('https://www.konga.com')
    slot_response_text = requests.get(url).text
    soup = BeautifulSoup(jumia_response.text, "html.parser")
    slot_soup = BeautifulSoup(slot_response_text, "html.parser")

    slot_holder = slot_soup.findChildren('div', {"class": "item-product"})[:3]
    print("slot_holder")
    print(slot_holder)
    for index, item in enumerate(slot_holder):
        p_url = item.findChild("a", {"class": "product-thumb-link"}).get("href")
        p_name = item.findChild("img", {"class": "product-image-photo"}).get("alt")
        image_url = item.findChild("img", {"class": "product-image-photo"}).get("src")
        price = item.findChild("span", {"class": "price"}).text
        p_id = "slot" + item.findChild("a", {"class": "quickview-link"}).get("data-id")
        print("-------------------------------------------------\n\n")
        print(p_url)
        print(p_name)
        print(p_id)
        print(image_url)
        print(price[:-3])
        print("-------------------------------------------------\n\n")
    holder = soup.find('div', {"class": "-pvxs"}).findChildren("article", {"class", "prd"})[:14]
    slide_info = {}
    for index, item in enumerate(holder):
        product_url = "https://www.jumia.com.ng" + item.findChild("a", {"class": "core"}).get("href")
        product_id = item.findChild("a", {"class": "core"}).get("data-id")
        image_url = item.findChild("a", {"class": "core"}).findChild("img", {"class": "img"}).get("data-src")
        product_price = item.findChild("a", {"class": "core"}).findChild("div", {"class": "prc"}).text
        product_name = item.findChild("a", {"class": "core"}).get("data-name")
        
        sub_dict = {}
        
        sub_dict["product_id"] = product_id
        sub_dict['product_name'] = product_name
        sub_dict['product_price'] = product_price
        sub_dict['image_url'] = image_url
        sub_dict['product_url'] = product_url
        sub_dict['product_store'] = 'Jumia'
        slide_info[index] = sub_dict
    
    
     
    if request.method == 'POST':
        # jumia_deals_url = 'https://www.jumia.com.ng'
        # konga_deals_url = 'https://www.konga.com/search?search=ProductOfTheWeek'
        # kara_deals_url = 'https://kara.com.ng'
        # kiaglo_deals_url = 'https://www.kaiglo.com/'
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data.get('search_field')
            return redirect('results', key=data)

    else:
        print("blank home page")
      
        form = SearchForm()
    return render(request, 'my_app/home.html', {'form': form, 'deals': slide_info})


def results(request, key):
    data = key
    jumia_search_string = data.replace(' ', '+')
    konga_search_string = data.replace(' ', '%20')
    kara_search_string = data.replace(' ', '+')
    jumia_url = "https://www.jumia.com.ng/catalog/?q="
    konga_url = "https://www.konga.com/search?search="
    kara_url = "https://kara.com.ng/catalogsearch/result/?q="
    kaiglo_url = "https://www.kaiglo.com/category/search?search="
    slot_url = "https://slot.ng/catalogsearch/result/?q="
    jumia_purl = jumia_url + jumia_search_string
    konga_purl = konga_url + konga_search_string
    kara_purl = kara_url + kara_search_string
    kaiglo_purl = kaiglo_url + kara_search_string
    slot_purl = slot_url + jumia_search_string
    

    jumia_data = getHTMLjumia(jumia_purl)
    print("jumia func completed")
    konga_data = getHTMLkonga(konga_purl)
    kara_data = getHTMLkara(kara_purl)
    slot_data = getHTMLslot(slot_purl)
    # kaiglo_data = getHTMLkaiglo(kaiglo_purl)

    context = {'jumia_data': jumia_data,
               'konga_data': konga_data, 'kara_data': kara_data, 'slot_data': slot_data
               }
    product_id = request.GET.get('product_id')
    product_name = request.GET.get('product_name')
    product_url = request.GET.get('product_url')
    product_price = request.GET.get('product_price')
    product_image_url = request.GET.get('product_image_url')
    # text_url = request.GET.get('product_url')
    if request.is_ajax():
        if request.user.is_authenticated:
            user = request.user
            print("-----------------------------------")
            print(product_id)
            print(product_name)
            print(product_url)
            print(product_price)
            print(product_image_url)
            print("-----------------------------------")
            SavedProduct.objects.create(product_id=product_id, name=product_name,
                                        price=product_price, image_url=product_image_url,
                                        product_url=product_url, owner=user, vendor='Jumia')
            print("saved object created successfully")
            messages.success(request, "Product Saved !!!")
            return JsonResponse({'status': 'saved completely'})

    return render(request, 'my_app/results.html', context)


@login_required
def cartpage(request):
    user = request.user
    carts = SavedProduct.objects.filter(owner=user)
    # for item in carts:
    #     print(item.name)
    # print(carts)
    # print(len(carts))
    return render(request, 'my_app/cart_list.html', {'carts': carts})


@login_required
def delete_cart(request, id):
    user = request.user
    if SavedProduct.objects.filter(owner=user, id=id).exists():
        SavedProduct.objects.filter(owner=user, id=id).delete()
        messages.success(request, 'Product deleted from cart')
        print("item successfully deleted")
        return redirect('cartpage')
    else:
        messages.success(request, 'Product does not exist')
        return redirect('cartpage')
    return redirect('cartpage')


# login function for the login page
def loginpage(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email_address')
            password = form.cleaned_data.get('password')
            email = email.lower()
            if Customuser.objects.filter(email=email).exists():
                custom_user = authenticate(
                    request, username=email, password=password)
                if custom_user is not None:
                    # messages.success(request, 'Login Succesful')
                    login(request, custom_user)
                    print("login successful")
                    # messages.success(request, f'Hello {custom_user.full_name} \n, You have been logged in successfully...would you love to fill in your interests?')
                    #print('user has been logged in')

                    return redirect('homepage')
                elif custom_user is None:
                    #print('message section')
                    messages.warning(
                        request, 'Incorrect email address or password')
            else:
                messages.warning(
                    request, 'Incorrect email address or password')
                return redirect('login_page')
    else:
        form = LoginForm()
    return render(request, 'my_app/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.warning(request, 'Logout successfully')
    return redirect('login_page')

# signup function for the signup page


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data.get('full_name')
            email = form.cleaned_data.get('email')
            phone_number = form.cleaned_data.get('phone_number')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')

            def verify_doesnt_exists():
                if Customuser.objects.filter(email=email).exists():
                    messages.warning(
                        request, 'This email has been used already')
                    print("email address already exists")
                    return False
                elif Customuser.objects.filter(phone_number=phone_number).exists():
                    messages.warning(
                        request, 'This phone number has already been used before')
                    print("phone_number already exists")
                    return False
                else:
                    return True
            if password1 == password2:
                if verify_doesnt_exists():
                    hashed = make_password(
                        password1, salt=None, hasher='default')

                    Customuser.objects.create(
                        username=email, full_name=full_name, email=email, phone_number=phone_number, password=hashed)
                    custom_user = authenticate(
                        username=email, password=password1,)
                    current_user = Customuser.objects.filter(
                        email=email).first()
                    current_instance = Customuser.objects.filter(email=email)
                    messages.success(request, 'Account Successfully Created')
                    return redirect('login_page')
            else:
                messages.warning(request, 'Passwords Don\'t Match')
    else:
        form = SignUpForm()
    return render(request, 'my_app/signup.html', {'form': form})
