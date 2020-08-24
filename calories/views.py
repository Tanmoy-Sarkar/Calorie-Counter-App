from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm,AddFoodForm
# Create your views here.

@login_required(login_url='login')
def HomePageView(request):
	return render(request, 'home.html')

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
				messages.success(request.user + "Your account was created")
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
def new_food(request):
    if request.method == 'POST':
        form = AddFoodForm(request.user,request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.person_of = request.user
            profile.save()
            return redirect('home')
    else:
        form = AddFoodForm(request.user)
    return render(request, 'add_food.html', {'form': form})