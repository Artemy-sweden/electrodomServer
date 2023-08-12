from rest_framework import serializers
from goods.models import Categories, Characteristic, GoodsCharacteristic

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


class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = '__all__'


class GoodsCharacteristicSerializer(serializers.ModelSerializer):
    characteristic = CharacteristicSerializer()

    class Meta:
        model = GoodsCharacteristic
        fields = ['characteristic', 'value']


class GoodsSerializer(serializers.ModelSerializer):
    characteristics = GoodsCharacteristicSerializer(many=True, source='goodscharacteristic_set')

    class Meta:
        model = Goods
        fields = ['id', 'name', 'provider_id', 'category_id', 'price', 'count', 'description', 'characteristics']

