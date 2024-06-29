from django.urls import path,include
from . import views

urlpatterns = [
    path('<str:user>', views.Home, name="HomePage"),
]