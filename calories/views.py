from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm,SelectFoodForm,AddFoodForm
from .models import *
from datetime import timedelta
from django.utils import timezone
from datetime import date
# Create your views here.

@login_required(login_url='login')
def HomePageView(request):
	
	calories = Profile.objects.filter(person_of=request.user).last()
	print(calories.id)
	print(calories.date)
	if date.today() > calories.date:
		profile=Profile.objects.create(person_of=request.user)
	some_day_last_week = timezone.now().date() - timedelta(days=7)
	monday_of_last_week = some_day_last_week - timedelta(days=(some_day_last_week.isocalendar()[2] - 1))
	monday_of_this_week = monday_of_last_week + timedelta(days=7)
	records=Profile.objects.filter(date__gte=monday_of_last_week, date__lt=monday_of_this_week,person_of=request.user)
	print(records)
	context = {
	'total_calorie':calories.total_calorie,
	'records':records
	}
	
	return render(request, 'home.html',context)

def RegisterPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:

		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request,"Account was created for "+ user)
				return redirect('login')

		context = {'form':form}
		return render(request,'register.html',context)


def LoginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:

		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(request,username=username,password=password)
			if user is not None:
				login(request,user)
				return redirect('home')
			else:
				messages.info(request,'Username or password is incorrect')
		context = {}
		return render(request,'login.html',context)

def LogOutPage(request):
	logout(request)
	return redirect('login')


@login_required
def select_food(request):
	person = Profile.objects.filter(person_of=request.user).last()
	food_items = Food.objects.filter(person_of=request.user)
	form = SelectFoodForm(request.user,instance=person)

	if request.method == 'POST':
		form = SelectFoodForm(request.user,request.POST,instance=person)
		if form.is_valid():
			
			form.save()
			return redirect('home')
	else:
		form = SelectFoodForm(request.user)

	context = {'form':form,'food_items':food_items}

	return render(request, 'select_food.html',context)

def add_food(request):
	food_items = Food.objects.filter(person_of=request.user)
	if request.method == 'POST':
		form = AddFoodForm(request.POST)
		if form.is_valid():
			profile = form.save(commit=False)
			profile.person_of = request.user
			profile.save()
			return redirect('add_food')
	else:
		form = AddFoodForm()

	context = {'form':form,'food_items':food_items}

	return render(request,'add_food.html',context)

