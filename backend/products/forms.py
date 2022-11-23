from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        models = Product
        fields = [
            'title',
            'content',
            'price'
        ]