from django.urls import path
from . import views as my_app_view

urlpatterns = [
    path('', my_app_view.home, name='homepage'),
    path('login/', my_app_view.loginpage, name='login_page'),
    path('logout/', my_app_view.logout_view, name='logout_page'),
    path('signup/', my_app_view.signup, name='signup_page'),
    path('results/<str:key>/', my_app_view.results, name='results'),
    path('cart/', my_app_view.cartpage, name='cartpage'),
    path('delete/cart/<int:id>/', my_app_view.delete_cart, name='delete_cart'),
    # path('testpage/', my_app_view.jsontest, name='jsonpage'),
]