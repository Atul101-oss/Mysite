from django.shortcuts import render

# Create your views here.

def profile(request, id):
    return render(request, 'Profile/profilePage.html')