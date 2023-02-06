from django import forms
from django.forms.models import ModelForm

class SearchForm(forms.Form):
    search_field = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Search Product', 'class': 'form-control mb-4', 'id': 'inputfield'}),
        label="")    
    
