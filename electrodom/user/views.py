from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

from user.models import User, Comment, Basket

from user.serializers import UserSerializer, CommentSerializer, BasketSerializer

from goods.models import Goods


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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








