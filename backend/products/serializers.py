from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    # my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'url',
            'pk',
            'title',
            'content',
            'price',
            'sale_price'
        ]

    def get_url(self, obj):
        return f"/api/products/{obj.pk}/"
    # def get_my_discount(self, obj):
    #     if not hasattr(obj, 'id'):
    #         return None
    #     if not isinstance(obj, Product):
    #         return None