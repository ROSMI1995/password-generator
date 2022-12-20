from django.shortcuts import render

# Create your views here.

def HomeView(request):
	return render(request, 'index.html')

def Password_display(request):
	return render(request, 'password_display.html')

