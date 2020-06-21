from django.urls import path
from . import views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/', views.user_update, name='user_update'),
    path('changepassword/', views.changepassword, name='changepassword'),
    path('orders/', views.user_orders, name='user_orders'),
    path('orderdetail/<int:id>', views.order_detail, name='order_detail'),
]