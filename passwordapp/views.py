from django.shortcuts import render
import random

# Create your views here.

def HomeView(request):
	return render(request, 'index.html')

def Password_display(request):
	characters =list('abcdefghijklmnopqrstuvwxyz')

	if request.GET.get('numbers'):
		characters.extend(list('0123456789'))
	if request.GET.get('uppercase'):
		characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

	if request.GET.get('special_character'):
		characters.extend(list('!@#$%^&*'))

	length = int(request.GET.get('length'))
	key =""
	for x in range(length):
		key+= random.choice(characters)
	return render(request, 'password_display.html',{'key':key})

