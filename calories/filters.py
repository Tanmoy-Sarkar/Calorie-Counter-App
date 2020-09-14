import django_filters
from django_filters import CharFilter
from .models import *

class FoodFilter(django_filters.FilterSet):
	food_name = CharFilter(field_name = 'name' , lookup_expr = 'icontains',label='search food items')
	class Meta:
		model = Food
		fields = ['food_name']
