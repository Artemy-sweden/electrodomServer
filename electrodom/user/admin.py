from django.contrib import admin

from user.models import User, Comment, Basket


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'photo', 'phone_number', 'address']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ['user', 'comment_text', 'comment_date']


@admin.register(Basket)
class CommentAdmin(admin.ModelAdmin):
    fields = ['user', 'goods', 'count']



