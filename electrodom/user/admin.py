from django.contrib import admin

from user.models import User, Comment, Basket


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'email', 'password', 'photo', 'phone_number', 'address')
    list_display = (User.__str__, 'first_name', 'last_name')
    User.__str__.short_description = 'Пользователь'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ('user', 'comment_text', 'comment_date')
    list_display = ('user', 'comment_date')


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    fields = ['user', 'goods', 'count']
    list_display = (Basket.__str__,)
    Basket.__str__.short_description = 'Корзина'




