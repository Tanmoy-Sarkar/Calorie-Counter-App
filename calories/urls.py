from django.urls import path

from .views import HomePageView,RegisterPage,LoginPage,LogOutPage,new_food,add_food

urlpatterns = [
	path('', HomePageView,name='home'),
	path('register/',RegisterPage,name='register'),
	path('login/',LoginPage,name='login'),
	path('logout/',LogOutPage,name='logout'),
	path('select_food/',new_food,name='select_food'),
	path('add_food/',add_food,name='add_food')
]