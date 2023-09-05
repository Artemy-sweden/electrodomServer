from rest_framework import serializers
from user.models import Basket, User, Comment
from goods.serializers import GoodsSerializer


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'comment_text', 'comment_date']
        read_only_fields = ['user']


class BasketSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer(required=False)

    class Meta:
        model = Basket
        fields = ['id', 'user', 'goods', 'count']


class UserSerializer(serializers.ModelSerializer):
    baskets = BasketSerializer(many=True, source='basket_set', required=False)

    extra_kwargs = {
        'password': {'write_only': True}
    }

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'photo', 'phone_number', 'address', 'baskets']


