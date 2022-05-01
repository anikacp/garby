from django.contrib import admin
from app.models import CUser
# Register your models here.

class CUserAdmin(admin.ModelAdmin):
    list_display = ("id", "username","full_name","points","redeemed")

admin.site.register(CUser, CUserAdmin)