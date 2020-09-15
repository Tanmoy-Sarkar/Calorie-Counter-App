from django.urls import path

from .views import HomePageView,LoginPage,LogOutPage,select_food,add_food,RegisterPage

urlpatterns = [
	path('', HomePageView,name='home'),
	path('login/',LoginPage,name='login'),
	path('logout/',LogOutPage,name='logout'),
	path('select_food/',select_food,name='select_food'),
	path('add_food/',add_food,name='add_food'),
	path('register/',RegisterPage,name='register'),
]