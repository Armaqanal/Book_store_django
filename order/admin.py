from django.contrib import admin
from .models import Order


# Register your models here.
# admin.site.register(Order)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["quantity", "book", "customer", "sale_price"]

    def sale_price(self, obj):
        return obj.calculate_sale_price()
