from django.contrib import admin
from account.models import Account

@admin.register(Account)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', )
    search_fields = ('username', )
