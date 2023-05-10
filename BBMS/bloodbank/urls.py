from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('bloodbank/', views.bloodbank, name='bloodbank'),
    path('bloodbank/details/<int:id>', views.details,name='details'),
]