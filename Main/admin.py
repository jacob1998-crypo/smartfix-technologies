from django.contrib import admin
from .models import Service
from .models import Laptop
from .models import Accessory

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    search_fields = ("title", "description")





@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
    search_fields = ("name", "specs")
    
    


@admin.register(Accessory)
class AccessoryAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "created_at")
    search_fields = ("name",)