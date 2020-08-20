from django.urls import path

from .views import HomePageView,RegisterPage,LoginPage

urlpatterns = [
	path('', HomePageView,name='home'),
	path('register/',RegisterPage,name='register'),
	path('login/',LoginPage,name='login')
]