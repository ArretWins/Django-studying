from django.contrib import admin

from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'created_at']
    inlines = [OrderItemInline]

admin.site.register(Order)
admin.site.register(OrderItem)