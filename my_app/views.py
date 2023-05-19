import random
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import SearchForm, LoginForm, SignUpForm
from .models import Customuser, SavedProduct
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from bs4 import BeautifulSoup
from django.contrib.auth.hashers import *
from django.contrib.auth.decorators import login_required
import requests
import re
import json


# Create your views here.

def getHTMLkonga(link):
    response = requests.get(link)
    # print("scraping Konga HTML......")
    # print(response.text.pre)
    soup = BeautifulSoup(response.text, "html.parser")
    # print(doc.prettify())
    # print(response.text)
    # print("print out...")
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
    # print(data_dict)
    # for i in data_dict:
    #     print("=====================")
    #     print(data_dict[i])
    #     print("=====================")
    return data_dict
    # print(check)
    # return soup.find('script', {"id": "__NEXT_DATA__"}).finc
    # return soup.prettify("utf-8")


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


def getHTMLjumia(link):
    user_agent = random.choice(user_agent_list)
    response = requests.get(link, headers={'User-Agent': user_agent})

    print("printing out the status of the request")
    print("--------------------------------")
    print(response.status_code)
    print(user_agent)
    print('--------------------------------')
    # print(response)
    # print("headers here")
    # print(response.headers)
    # print("done with HTMl")
    soup = BeautifulSoup(response.text, "html.parser")
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


def getHTMLkara(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
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
    # print("--------------------------------------------------------------")
    # print(product_id)
    # print(product_price)
    # print(product_url)
    # print(image_url)
    # print(product_name)
    # print("--------------------------------------------------------------")


def getHTMLkiaglo(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
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


slide_data = {
    1: {
        'name': 'Men Athletic Sneaker Elastic Running Casual Shoes',
        'price': 'N3,800',
        'image_url': 'https://ng.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/14/160244/1.jpg?0532',
        'vendor': 'Jumia',
    },
    2: {
        'name': '2 In 1 Men\'s Short Sleeve Shorts Set - White',
        'price': 'N3,000',
        'image_url': 'https://ng.jumia.is/unsafe/fit-in/500x500/filters:fill(white)/product/76/202776/1.jpg?0581',
        'vendor': 'Jumia',
    },
    3: {
        'name': 'APC Back-UPS 1400VA,230V, AVR,IEC Sockets(BX1400UI)',
        'price': 'N89,120',
        'image_url': 'https://www-konga-com-res.cloudinary.com/w_auto,f_auto,fl_lossy,dpr_auto,q_auto/media/catalog/product/Q/M/_1622031731.jpg',
        'vendor': 'Konga',
    },
    4: {
        'name': 'HP LaserJet M443NDA Multifunction Printer-8AF72A',
        'price': 'N839,500',
        'image_url': 'https://kara.com.ng/media/catalog/product/cache/3d615c6d9644c5c38c7d599cf735420f/h/p/hp_m443nda_printer_2.jpg',
        'vendor': 'Kara',
    },

    5: {
        'name': 'elepaq roller item',
        'price': 'N120, 000',
        'image_url': 'https://ng.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/14/160244/1.jpg?0532',
        'vendor': 'Jumia',
    },
    6: {
        'name': 'elepaq roller item',
        'price': 'N120, 000',
        'image_url': 'https://ng.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/14/160244/1.jpg?0532',
        'vendor': 'Jumia',
    },
    7: {
        'name': 'elepaq roller item',
        'price': 'N120, 000',
        'image_url': 'https://ng.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/14/160244/1.jpg?0532',
        'vendor': 'Jumia',
    },
    8: {
        'name': 'elepaq roller item',
        'price': 'N120, 000',
        'image_url': 'https://ng.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/14/160244/1.jpg?0532',
        'vendor': 'Jumia',
    },
    9: {
        'name': 'elepaq roller item',
        'price': 'N120, 000',
        'image_url': 'https://ng.jumia.is/unsafe/fit-in/300x300/filters:fill(white)/product/14/160244/1.jpg?0532',
        'vendor': 'Jumia',
    },
}


def home(request):
    if request.method == 'POST':
        jumia_deals_url = 'https://www.jumia.com.ng'
        konga_deals_url = 'https://www.konga.com/search?search=ProductOfTheWeek'
        kara_deals_url = 'https://kara.com.ng'
        kiaglo_deals_url = ''
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data.get('search_field')
            return redirect('results', key=data)

    else:
        form = SearchForm()
    return render(request, 'my_app/home.html', {'form': form, 'deals': slide_data})


def results(request, key):
    data = key
    jumia_search_string = data.replace(' ', '+')
    konga_search_string = data.replace(' ', '%20')
    kara_search_string = data.replace(' ', '+')
    jumia_url = "https://www.jumia.com.ng/catalog/?q="
    konga_url = "https://www.konga.com/search?search="
    kara_url = "https://kara.com.ng/catalogsearch/result/?q="
    jumia_purl = jumia_url + jumia_search_string
    konga_purl = konga_url + konga_search_string
    kara_purl = kara_url + kara_search_string

    jumia_data = getHTMLjumia(jumia_purl)
    konga_data = getHTMLkonga(konga_purl)
    kara_data = getHTMLkara(kara_purl)

    context = {'jumia_data': jumia_data,
               'konga_data': konga_data, 'kara_data': kara_data
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

    # print(key)
    # print(jumia_data)
    # print(konga_data)
    # for item in jumia_data:
    #     print(konga_data[item]['product_name'])
    # #     print("----------------------------------")
    # for key, value in jumia_data.items():
    #     # print(key)
    #     # print(value.tester)
    #     print('-------------------------------')
    #     # for key, value in value.items():
    #     #     print(key)
    #     #     print(value)
    #     #     print('-------------------------------')
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
                    print("login suuccessful")
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
