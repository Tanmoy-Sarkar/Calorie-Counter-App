from django.shortcuts import render

# Create your views here.

def HomePageView(request):
	return render(request, 'home.html')