from rest_framework import serializers
from decimal import Decimal
from .models import MenuItem, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "slug",
            "title"
        ]

class MenuItemSerilaizer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source="inventory")
    price_after_tax = serializers.SerializerMethodField(method_name="calculate_tax")
    category = CategorySerializer(read_only=True)
    category_id = CategorySerializer(write_only=True)
    class Meta:
        model =  MenuItem
        fields = [
            "id",
            "title",
            "price",
            "stock",
            "price_after_tax",
            "category",
            "category_id"
        ]
    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)
