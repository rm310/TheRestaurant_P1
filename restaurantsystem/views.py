from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from restaurantsystem.models import DishesMenu, BookingPlace, ContactInfo, Orders
from .forms import DishesMenuPage

def dishes_menu(request):
    form = DishesMenuPage()

    if request.method == "POST":
        form = DishesMenuPage(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dishes_menu')
    query = request.GET.get('q', '')
    dishes = DishesMenu.objects.filter(dish_name__icontains=query) if query else DishesMenu.objects.all().order_by('id')
    paginator = Paginator(dishes, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'restaurantsystem/dishesmenu.html', {'form': form, 'dishes': page_obj, 'query': query})


def bookingsystem(request):
    bookings = BookingPlace.objects.all().order_by('id')
    paginator = Paginator(bookings, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'restaurantsystem/bookingsystem.html', {'bookings': page_obj})

def contactinfos(request):
    cinfos = ContactInfo.objects.all().order_by('id')
    paginator = Paginator(cinfos, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'restaurantsystem/contactinfos.html', {'cinfos': page_obj})


def orders(request):
    orderdetails = Orders.objects.prefetch_related('orderdetails_set__dish').all().order_by('id')
    paginator = Paginator(orderdetails, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'restaurantsystem/orders.html', {'orderdetails': page_obj})