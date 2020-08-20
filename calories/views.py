from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import CreateUserForm
# Create your views here.

def HomePageView(request):
	return render(request, 'home.html')

def RegisterPage(request):
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request,user + "Your account was created")
			return redirect('login')

	context = {'form':form}
	return render(request,'register.html',context)


def LoginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('home')
	context = {}
	return render(request,'login.html',context)