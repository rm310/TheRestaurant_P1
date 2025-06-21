
from django.urls import path

from .views import dishes_menu, bookingsystem, orders, contactinfos


# def index(request):
#     html_ = (
#         '<h1>Welcome to the Restaurant System!</h1> <br>'
#         '<a href = "http://127.0.0.1:8000/dishes_menu/">dishes menu</a> <br>'
#         '<a href = "http://127.0.0.1:8000/booking_place/">booking place</a> <br>'
#         '<a href = "http://127.0.0.1:8000/contact_informations/">contact informations</a> <br>'
#         '<a href = "http://127.0.0.1:8000/order_details/">order details</a> <br>'
#     )
#     return HttpResponse(html_)
urlpatterns = [
    path('dishes_menu/', dishes_menu, name='dishes_menu'),
    path('bookings/', bookingsystem, name='booking_place'),
    path('orders/', orders, name='order_details'),
    path('contactinfos/', contactinfos, name='contact_informations')
]