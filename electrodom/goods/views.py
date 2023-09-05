from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from goods.models import Categories
from goods.serializers import CategorySerializer, GoodsShortSerializer
from goods.serializers import ProviderSerializer

from goods.models import Providers

from goods.serializers import GoodsSerializer

from goods.models import Goods


class CategoriesViewSet(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer


class ProvidersViewSet(ModelViewSet):
    queryset = Providers.objects.all()
    serializer_class = ProviderSerializer


class GoodsViewSet(ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category_id', 'price', ]
    search_fields = ['description', 'name']
    ordering_fields = ['id', 'price']

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return GoodsSerializer
        else:
            return GoodsShortSerializer






