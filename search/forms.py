from django import forms

class SearchQuery(forms.Form): 
    """ Simple form to get search query """
    query = forms.CharField(min_length=3, max_length=20)