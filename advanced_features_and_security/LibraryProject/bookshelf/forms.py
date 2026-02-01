# LibraryProject/bookshelf/forms.py
from django import forms

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)