from django.contrib import admin

from user.models import User, Comment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'photo', 'phone_number', 'address']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ['user', 'comment_text', 'comment_date']
