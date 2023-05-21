from django import forms
from django.forms.models import ModelForm


class SearchForm(forms.Form):
    search_field = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Search Product', 'class': 'form-control mb-4', 'id': 'inputfield'}),
        label="")


class LoginForm(forms.Form):
    email_address = forms.CharField(
        widget=forms.EmailInput(attrs={
                                'placeholder': 'Email Address', 'class': 'form-control mb-4', 'id': 'inputfield'}),
        label="")
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control ', 'id': 'inputfield'}), label="")


class SignUpForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={
                               'placeholder': 'Full Name', 'class': 'form-control mb-4', 'id': 'inputfullname'}),
        label="")

    email = forms.CharField(
        widget=forms.EmailInput(attrs={
                                'placeholder': 'Email Address', 'class': 'form-control mb-4', 'id': 'inputemail'}),
        label="")
    phone_number = forms.CharField(
        widget=forms.NumberInput(attrs={
                                 'placeholder': 'Phone Number', 'class': 'form-control mb-4', 'id': 'inputphonenumber'}),
        label="")

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter Password', 'class': 'form-control mb-4 ', 'id': 'inputpassword'}),
        label="")
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter Password Again', 'class': 'form-control mb-4', 'id': 'inputpassword'}),
        label="")
