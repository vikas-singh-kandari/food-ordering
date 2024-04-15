from django.contrib import admin
from .models import addshop

class AddShopAdmin(admin.ModelAdmin):
    list_display = ['shop_name', 'shop_img', 'shop_contact', 'shop_address']  # Display these fields in the admin list view
    search_fields = ['shop_name']  # Enable searching by shop name
    list_filter = ['shop_contact']  # Add filters for shop contact

# Register your model with the custom admin class
admin.site.register(addshop, AddShopAdmin)
