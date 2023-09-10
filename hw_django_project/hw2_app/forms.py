from django import forms

class ProductImageForm(forms.Form):
    image = image = forms.ImageField()