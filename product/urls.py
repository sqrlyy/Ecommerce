from django.urls import path
from . import views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addcomment/<int:id>', views.addcoment, name='addcommment')
]