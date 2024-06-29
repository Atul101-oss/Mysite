from django.shortcuts import render, HttpResponse

# Create your views here.
def Home(request, user):
    return render(request, 'Home/HomePage.html')