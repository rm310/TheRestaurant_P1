from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from restaurantsystem.models import DishesMenu, BookingPlace, ContactInfo, Orders, OrderDetails
from .forms import DishesMenuPage, BookingSystemPage, ContactInfoPage, OrdersPage, OrderDetailsPage, OrderDetailsFormSet


@permission_required('restaurantsystem.can_publish_dish', raise_exception=True)
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
    show_form = request.GET.get('create') == '1'
    create_form = BookingSystemPage()
    edit_booking = None
    edit_form = None
    if 'edit' in request.GET:
        booking_id = request.GET.get('edit')
        if booking_id:
            edit_booking = get_object_or_404(BookingPlace, id=booking_id)
            edit_form = BookingSystemPage(instance=edit_booking)
            show_form = False
    if request.method == "POST":
        action = request.POST.get('action')
        booking_id = request.POST.get('booking_id')
        if action == 'create':
            create_form = BookingSystemPage(request.POST)
            if create_form.is_valid():
                create_form.save()
                return redirect('booking_place')
        elif action == 'edit' and booking_id:
            booking = get_object_or_404(BookingPlace, id=booking_id)
            edit_form = BookingSystemPage(request.POST, instance=booking)

            if edit_form.is_valid():
                edit_form.save()
                return redirect('booking_place')
            else:
                print("Edit form errors:", edit_form.errors)
                edit_booking = booking
                show_form = False
        elif action == 'delete' and booking_id:
            booking = get_object_or_404(BookingPlace, id=booking_id)
            booking.delete()
            return redirect('booking_place')
    query = request.GET.get('q', '')
    bookings = BookingPlace.objects.filter(customers_name__icontains=query)if query else BookingPlace.objects.all().order_by('id')
    paginator = Paginator(bookings, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'restaurantsystem/bookingsystem.html', {'create_form': create_form,'show_form': show_form, 'bookings': page_obj, 'query': query, 'edit_form': edit_form, 'edit_booking_id': edit_booking.id if edit_booking else None})

def contactinfos(request):
    show_form = request.GET.get('create') == '1'
    create_form = ContactInfoPage()
    edit_cinfo = None
    edit_form = None
    if 'edit' in request.GET:
        cinfo_id = request.GET.get('edit')
        if cinfo_id:
            edit_cinfo = get_object_or_404(ContactInfo, id=cinfo_id)
            edit_form = ContactInfoPage(instance=edit_cinfo)
            show_form = False
    if request.method == "POST":
        action = request.POST.get('action')
        cinfo_id = request.POST.get('cinfo_id')
        if action == 'create':
            create_form = ContactInfoPage(request.POST)
            if create_form.is_valid():
                create_form.save()
                return redirect('contact_informations')
        elif action == 'edit' and cinfo_id:
            cinfo = get_object_or_404(ContactInfo, id=cinfo_id)
            edit_form = ContactInfoPage(request.POST, instance=cinfo)

            if edit_form.is_valid():
                edit_form.save()
                return redirect('contact_informations')
            else:
                print("Edit form errors:", edit_form.errors)
                edit_cinfo = cinfo
                show_form = False
        elif action == 'delete' and cinfo_id:
            cinfo = get_object_or_404(ContactInfo, id=cinfo_id)
            cinfo.delete()
            return redirect('contact_informations')
    query = request.GET.get('q', '')
    cinfos = ContactInfo.objects.all().filter(phone_number1__icontains=query)if query else ContactInfo.objects.all().order_by('id')
    paginator = Paginator(cinfos, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'restaurantsystem/contactinfos.html', {'create_form': create_form, 'edit_form': edit_form, 'query': query,'cinfos': page_obj, 'show_form': show_form, 'edit_cinfo_id': edit_cinfo.id if edit_cinfo else None})


def orders(request):
    show_form = request.GET.get('create') == '1'
    create_form = OrdersPage()
    create_formset = OrderDetailsFormSet(queryset=OrderDetails.objects.none())
    edit_order = None
    edit_form = None
    edit_formset = None
    dishes = DishesMenu.objects.all()

    if 'edit' in request.GET:
        order_id = request.GET.get('edit')
        if order_id:
            edit_order = get_object_or_404(Orders, id=order_id)
            edit_form = OrdersPage(instance=edit_order)
            edit_formset = OrderDetailsPage(instance=edit_order)
            show_form = False

    if request.method == "POST":
        action = request.POST.get('action')
        order_id = request.POST.get('order_id')

        if action == 'create':
            create_form = OrdersPage(request.POST)
            create_formset = OrderDetailsFormSet(request.POST)
            if create_form.is_valid() and create_formset.is_valid():
                order = create_form.save()
                for form in create_formset:
                    if form.cleaned_data:
                        detail = form.save(commit=False)
                        detail.order = order
                        detail.save()
                return redirect('order_details')
            else:
                print("Create form errors:", create_form.errors, create_formset.errors)

        elif action == 'edit' and order_id:
            order = get_object_or_404(Orders, id=order_id)
            edit_form = OrdersPage(request.POST, instance=order)
            edit_formset = OrderDetailsPage(request.POST, instance=order)
            if edit_form.is_valid() and edit_formset.is_valid():
                edit_form.save()
                edit_formset.save()
                return redirect('order_details')
            else:
                print("Edit form errors:", edit_form.errors, edit_formset.errors)
                edit_order = order
                show_form = False

        elif action == 'delete' and order_id:
            order = get_object_or_404(Orders, id=order_id)
            order.delete()
            return redirect('order_details')
    query = request.GET.get('q', '')
    orderdetails = Orders.objects.all().filter(orderers_name__icontains=query)if query else Orders.objects.all().order_by('id')
    paginator = Paginator(orderdetails, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'restaurantsystem/orders.html', {'create_form': create_form, 'create_formset': create_formset, 'edit_formset': edit_formset, 'edit_form': edit_form,'query': query, 'orderdetails': page_obj, 'dishes': dishes,  'show_form': show_form, 'edit_order_id': edit_order.id if edit_order else None})
