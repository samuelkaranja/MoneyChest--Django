from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request, 'Box/index.html')

def Deposit(request):
    return render(request, 'Box/deposit.html')

def PlayChests(request):
    return render(request, 'Box/play-chests.html')