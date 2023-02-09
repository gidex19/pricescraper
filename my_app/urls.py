from django.urls import path
from . import views as my_app_view

urlpatterns = [
    path('home/', my_app_view.home, name='homepage'),
    # path('testpage/', my_app_view.jsontest, name='jsonpage'),
]