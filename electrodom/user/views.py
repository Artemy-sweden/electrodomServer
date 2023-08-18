from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

from user.models import User, Comment, Basket
from user.permissions import AllowPostWithoutAutheticated

from user.serializers import UserSerializer, CommentSerializer, BasketSerializer

from goods.models import Goods


def create_token(func):
    def wrapper(request, *args, **kwargs):
        data = func(request, *args, **kwargs)
        user_id = data.data['id']
        user = User.objects.get(id=user_id)
        token = Token.objects.create(user=user)
        data.data['token'] = token.key
        return data
    return wrapper


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowPostWithoutAutheticated,)

    @create_token
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        token = self.request.auth
        user = Token.objects.get(key=token).user
        queryset = User.objects.filter(id=user.id)
        return queryset


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BasketViewSet(ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

    def create(self, request, *args, **kwargs):
        print('------------------------------------------')
        print(request.data['user'])
        print('------------------------------------------')
        user = User.objects.get(id=request.data['user'])
        goods = Goods.objects.get(id=request.data['goods'])
        baskets = Basket.objects.filter(user=user, goods=goods)

        if not baskets.exists():
            basket = Basket.objects.create(user=user, goods=goods, count=request.data['count'])
        else:
            basket = baskets.first()
            basket.count += int(request.data['count'])
            basket.save()
        return Response(BasketSerializer(basket).data)








