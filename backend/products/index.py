from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Product

@register(Product)
class ProductIndex(AlgoliaIndex):
    schould_index = 'is_public'
    fields = [
        'title',
        'content',
        'price',
        'user',
        'public'
    ]