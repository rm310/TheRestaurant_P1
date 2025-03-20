from django.contrib import admin
from .models import DishesMenu, ContactInfo, BookingPlace, Orders, OrderDetails

admin.site.register(DishesMenu)
admin.site.register(ContactInfo)
admin.site.register(BookingPlace)

class OrderDetailsInLine(admin.TabularInline):
    model = OrderDetails
    extra = 1

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'orderers_name', 'orderers_phone', 'order_datetime', 'total_price')
    inlines = [OrderDetailsInLine]

admin.site.register(Orders, OrdersAdmin)
admin.site.register(OrderDetails)

