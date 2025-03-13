from django.contrib import admin
from .models import  DishesMenu, ContactInfo, BookingPlace, Orders

admin.site.register(DishesMenu)
admin.site.register(ContactInfo)
admin.site.register(BookingPlace)
admin.site.register(Orders)
