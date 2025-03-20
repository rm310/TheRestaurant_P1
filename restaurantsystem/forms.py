from django import forms
from .models import DishesMenu

class DishesMenuPage(forms.ModelForm):
    class Meta:
        model = DishesMenu
        fields = ['dish_name', 'description', 'price', 'portion', 'specification']