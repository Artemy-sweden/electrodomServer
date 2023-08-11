from django.contrib import admin

from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'photo', 'phone_number', 'address']
