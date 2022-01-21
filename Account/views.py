from django.shortcuts import render

# Create your views here.

def Register(request):
    return render(request, 'Account/register.html')

def Login(request):
    return render(request, 'Account/login.html')