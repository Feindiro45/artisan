from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'app/login.html')
        else:
            messages.error(request, 'Mauvaise authentification')
            return redirect('home')
    return render(request, 'app/index.html')

def logOut(request):
    logout(request)
    messages.success(request, 'Vous avez été bien déconnecter')
    return redirect('home')


