from decimal import Decimal
from django.db import models

class DishesMenu(models.Model):

    class Specifications(models.TextChoices):
        SPICY = 'SP', 'Spicy'
        MEDIUM_HOT = 'MH', 'Medium Hot'
        ORDINARY = 'OR', 'Ordinary'
        VEGAN = 'VG', 'Vegan'
        CONTAINS_NUTS = 'CN', 'Contains Nuts'
        CONTAINS_CITRUS = 'CC', 'Contains Citrus'

    dish_name = models.CharField(max_length=20)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=3)
    portion = models.CharField(max_length=30)
    specification = models.CharField(max_length=2,
                                     choices=Specifications.choices,
                                     default=Specifications.ORDINARY)

    def __str__(self):
        return self.dish_name

    class Meta:
        permissions = [
            {'can_publish_dish', 'Can publish dish'}
        ]


class ContactInfo(models.Model):
    phone_number1 = models.CharField(max_length=30, unique=True)
    phone_number2 = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=50, unique=True)
    social_account1 = models.CharField(max_length=50, unique=True)
    social_account2 = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.phone_number1

class BookingPlace(models.Model):

    class Specifications(models.TextChoices):
        WHEELCHAIR = 'WC', 'Wheelchair'
        CHILDSEAT = 'CS', 'Child Seat'
        EVENT = 'EV', 'Event'
        PEOPLEWITHDESABILITIES = 'PD', 'People with Disabilities'
        NOSPECIFICATIONS = 'NS', 'No Specifications'

    date_time = models.DateTimeField(auto_now_add=True, unique=True)
    place_for = models.IntegerField()
    phone_number = models.CharField(max_length=30)
    customers_name = models.CharField(max_length=20)
    specifications = models.CharField(max_length=2,
                                      choices=Specifications.choices,
                                      default=Specifications.NOSPECIFICATIONS)

    def __str__(self):
        return self.customers_name

class Orders(models.Model):
    orderers_name = models.CharField(max_length=30)
    orderers_phone = models.CharField(max_length=30)
    delivery_address = models.TextField()
    order_datetime = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        total = sum(item.total_price() for item in self.orderdetails_set.all())
        return round(total, 2)

    def __str__(self):
        return f'Order {self.id} - {self.orderers_name}'

class OrderDetails(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    dish = models.ForeignKey(DishesMenu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return round(Decimal(self.dish.price) * self.quantity, 2)

    def __str__(self):
        return f'{self.quantity} x {self.dish.dish_name} in Order {self.order_id}'
