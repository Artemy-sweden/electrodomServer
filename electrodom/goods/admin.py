from django.contrib import admin

from goods.models import Categories


@admin.register(Categories)
class SitePhotosAdmin(admin.ModelAdmin):
    fields = ('category_name', )
