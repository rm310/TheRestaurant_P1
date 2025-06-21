from django import forms
from .models import DishesMenu, BookingPlace, ContactInfo, Orders, OrderDetails
from django.forms import modelformset_factory


class DishesMenuPage(forms.ModelForm):
    class Meta:
        model = DishesMenu
        fields = ['dish_name', 'description', 'price', 'portion', 'specification']

    def __init__(self, *args, **kwargs):
        super(DishesMenuPage, self).__init__(*args, **kwargs)

        self.fields['dish_name'].required = True
        self.fields['price'].required = True
        self.fields['dish_name'].min_length = 2
        self.fields['dish_name'].max_length = 20
        self.fields['dish_name'].error_message = {
            'required': 'Dish name is mandatory',
            'min_length': 'Name of dish should contain at least 2 elements',
            'max_length': 'Name of dish should contain less than 20 elements'
        }

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 1.000:
            raise forms.ValidationError("Price should be more than 1.000 sums")
        return price


class BookingSystemPage(forms.ModelForm):
    class Meta:
        model = BookingPlace
        fields = ['place_for', 'phone_number', 'customers_name', 'specifications']

    # def __init__(self, *args, **kwargs):
    #     super(ContactInfoPage, self).__init__(*args, **kwargs)
    #
    #     self.fields['email'].required = True
    #     self.fields['email'].error_messages = {
    #         'required': 'Email is mandatory',
    #         'invalid': 'Please enter valid email'
        # }

class ContactInfoPage(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['phone_number1', 'phone_number2', 'email', 'social_account1', 'social_account2']




class OrdersPage(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['orderers_name', 'orderers_phone', 'delivery_address']


class OrderDetailsPage(forms.ModelForm):
    class Meta:
        model = OrderDetails
        fields = ['dish', 'quantity']


OrderDetailsFormSet = modelformset_factory(OrderDetails, form=OrderDetailsPage, extra=10)
