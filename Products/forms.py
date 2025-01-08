from django import forms

class SearchForm(forms.Form) :
    content = forms.CharField(max_length=100)
