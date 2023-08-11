from rest_framework import serializers
from goods.models import Categories

from goods.models import Providers

from goods.models import Goods


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'category_name']


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Providers
        fields = ['id', 'provider_name']


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = ['id', 'name', 'provider_id', 'category_id', 'price', 'count', 'description']
