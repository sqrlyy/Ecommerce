from django.urls import path
from . import views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addtoshopcart/<int:id>', views.addtoshopcart, name='addtoshopcart'),
    path('deletefromshopcart/<int:id>', views.deletefromshopcart, name='deletefromshopcart'),
    path('orderproduct/', views.orderproduct, name='orderproduct')
]