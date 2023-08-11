from django.contrib import admin

from goods.models import Categories

from goods.models import Providers

from goods.models import Goods


@admin.register(Categories)
class SitePhotosAdmin(admin.ModelAdmin):
    fields = ('category_name', )


@admin.register(Providers)
class SitePhotosAdmin(admin.ModelAdmin):
    fields = ('provider_name', )


@admin.register(Goods)
class SitePhotosAdmin(admin.ModelAdmin):
    fields = ('name', 'provider_id', 'category_id', 'price', 'count', 'description')
