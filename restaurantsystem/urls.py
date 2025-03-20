from django.http import HttpResponse
from django.urls import path
from .views import dishes_menu, bookingsystem, orders, contactinfos


def index(request):
    html_ = (
        '<h1>Welcome to the Restaurant System!</h1> <br>'
        '<a href = "http://127.0.0.1:8000/dishesmenu/">dishes menu</a> <br>'
        '<a href = "http://127.0.0.1:8000/bookings/">booking place</a> <br>'
        '<a href = "http://127.0.0.1:8000/contactinfos/">contact informations</a> <br>'
        '<a href = "http://127.0.0.1:8000/orders/">order details</a> <br>'
    )
    return HttpResponse(html_)
urlpatterns = [
    path('', index, name='index'),
    path('dishesmenu/', dishes_menu, name='dishes_menu'),
    path('bookings/', bookingsystem, name='booking_place'),
    path('orders/', orders, name='order details'),
    path('contactinfos/', contactinfos, name='contact_informations')
]