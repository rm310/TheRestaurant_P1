from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from restaurantsystem.models import DishesMenu, BookingPlace, ContactInfo, Orders, OrderDetails
from .forms import DishesMenuPage, BookingSystemPage, ContactInfoPage, OrdersPage, OrderDetailsPage

def dishes_menu(request):
    show_form = request.GET.get('create') == '1'
    create_form = DishesMenuPage()
    edit_dish = None
    edit_form = None
    if 'edit' in request.GET:
        dish_id = request.GET.get('edit')
        if dish_id:
            edit_dish = get_object_or_404(DishesMenu, id=dish_id)
            edit_form = DishesMenuPage(instance=edit_dish)
            show_form = False
    if request.method == "POST":
        action = request.POST.get('action')
        dish_id = request.POST.get('dish_id')
        if action == 'create':
            create_form = DishesMenuPage(request.POST)
            if create_form.is_valid():
                create_form.save()
                return redirect('dishes_menu')
        elif action == 'edit' and dish_id:
            dish = get_object_or_404(DishesMenu, id=dish_id)
            edit_form = DishesMenuPage(request.POST, instance=dish)

            if edit_form.is_valid():
                edit_form.save()
                return redirect('dishes_menu')
            else:
                print("Edit form errors:", edit_form.errors)
                edit_dish = dish
                show_form = False
        elif action == 'delete' and dish_id:
            dish = get_object_or_404(DishesMenu, id=dish_id)
            dish.delete()
            return redirect('dishes_menu')

    query = request.GET.get('q', '')
    dishes = DishesMenu.objects.filter(dish_name__icontains=query) if query else DishesMenu.objects.all().order_by('id')
    paginator = Paginator(dishes, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'restaurantsystem/dishesmenu.html', {'creat_form': create_form, 'show_form': show_form,'dishes': page_obj, 'query': query, 'edit_form': edit_form, 'edit_dish_id': edit_dish.id if edit_dish else None})


def bookingsystem(request):
    form = BookingSystemPage()
    if request.method == "POST":
        form = BookingSystemPage(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookingsystem')
        else:
            print("Form errors:", form.errors)
    query = request.GET.get('q', '')
    bookings = BookingPlace.objects.filter(customers_name__icontains=query)if query else BookingPlace.objects.all().order_by('id')
    paginator = Paginator(bookings, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'restaurantsystem/bookingsystem.html', {'form': form, 'bookings': page_obj, 'query': query})

def contactinfos(request):
    form = ContactInfo()
    if request.method == "POST":
        form = ContactInfoPage(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contactinfos')
        else:
            print("Form errors:", form.errors)
    query = request.GET.get('q', '')
    cinfos = ContactInfo.objects.all().filter(phone_number1__icontains=query)if query else ContactInfo.objects.all().order_by('id')
    paginator = Paginator(cinfos, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'restaurantsystem/contactinfos.html', {'form': form, 'query': query,'cinfos': page_obj})


def orders(request):
    form = Orders()
    formset = OrderDetails.objects.none()
    dishes = DishesMenu.objects.all()
    if request.method == "POST":
        form = OrdersPage(request.POST)
        formset = OrderDetailsPage(request.POST)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('orders')
        else:
            print("Form errors:", form.errors)
    query = request.GET.get('q', '')
    orderdetails = Orders.objects.all().filter(orderers_name__icontains=query)if query else Orders.objects.all().order_by('id')
    paginator = Paginator(orderdetails, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'restaurantsystem/orders.html', {'form': form, 'query': query, 'orderdetails': page_obj, 'dishes': dishes})
