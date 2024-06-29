from django.urls import path,include
from . import views

urlpatterns = [
    
    path('<str:id>', views.profile, name="profilePage"),
]