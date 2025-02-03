from django.contrib import admin
from apis.users.models import User
from django.contrib.auth.models import Group

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'address', 'phone_number')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('username', 'address', 'phone_number')
