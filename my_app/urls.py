from django.urls import path
from . import views as my_app_view

urlpatterns = [
    path('', my_app_view.home, name='homepage'),
    path('login/', my_app_view.loginpage, name='login_page'),
    path('signup/', my_app_view.signup, name='signup_page'),
    path('results/<str:key>/', my_app_view.results, name='results'),
    # path('testpage/', my_app_view.jsontest, name='jsonpage'),
]