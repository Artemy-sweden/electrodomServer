from django.contrib import admin

from goods.models import Categories

from goods.models import Providers


@admin.register(Categories)
class SitePhotosAdmin(admin.ModelAdmin):
    fields = ('category_name', )


@admin.register(Providers)
class SitePhotosAdmin(admin.ModelAdmin):
    fields = ('provider_name', )
