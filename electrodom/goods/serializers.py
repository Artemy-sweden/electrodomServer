from rest_framework import serializers
from goods.models import Categories, Characteristic, GoodsCharacteristic, Photo

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


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'path']


class GoodsSerializer(serializers.ModelSerializer):
    characteristics = GoodsCharacteristicSerializer(many=True, source='goodscharacteristic_set', required=False)
    category = CategorySerializer(source='category_id')

    product_images = PhotoSerializer(many=True, source='photo_set.filter(for_card=True)')
    general_images = PhotoSerializer(many=True, source='photo_set.filter(for_card=False)')

    class Meta:
        model = Goods
        fields = ['id', 'name', 'provider_id', 'category', 'price', 'count', 'description',
                  'characteristics', 'product_images', 'general_images']
