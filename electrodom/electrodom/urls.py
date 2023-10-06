from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from .yasg import urlpatterns as doc_urls

from user.views import UserViewSet, CommentViewSet, BasketViewSet
from goods.views import GoodsViewSet


router = DefaultRouter()
# router.register('categories', CategoriesViewSet)
router.register('users', UserViewSet)
router.register('comments', CommentViewSet)
# router.register('providers', ProvidersViewSet)
router.register('baskets', BasketViewSet)
router.register('goods', GoodsViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
] + router.urls

urlpatterns += doc_urls
