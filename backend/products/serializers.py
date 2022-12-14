from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from .validators import *

from api.serializers import UserPublicSerializer

class ProductSerializer(serializers.ModelSerializer):
    # my_discount = serializers.SerializerMethodField(read_only=True)
    user = UserPublicSerializer(read_only = True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field= 'pk'
    )
    title = serializers.CharField(validators=[validate_title_no_hello, unique_product_title])
    # email = serializers.EmailField(write_only=True)
    body = serializers.CharField(source = 'content')
    class Meta:
        model = Product
        fields = [
            'user',
            'url',
            'edit_url',
            'pk',
            'title',
            'body',
            'price',
            'sale_price'
        ]

    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name")
    #     return value

    # def create(self, validated_data):
    #     #return Product.objects.create(**validated_data)
    #     # email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     return obj
    #
    # def update(self, instance, validated_data):
    #     instance.title = validated_data.get('email')
    #     return instance

    def get_edit_url(self, obj):
        #return f"/api/products/{obj.pk}/"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)

    # def get_my_discount(self, obj):
    #     if not hasattr(obj, 'id'):
    #         return None
    #     if not isinstance(obj, Product):
    #         return None