from django.contrib import admin
from .models import Auction

# Register your models here.
@admin.register(Auction)
class UserAdmin(admin.ModelAdmin):
    list_display = ("item_name","start_time","end_time","start_price","winner")


