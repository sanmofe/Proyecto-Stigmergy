from django.urls import path
from . import views

urlpatterns=[
    path('restaurante/list/',views.get_restaurantees, name= 'restauranteList'),
    path('restaurante/get/<int:id>/', views.get_restaurante, name= 'restaurante'), 
    path('restaurante/delete/<int:id>/', views.delete_restaurante, name= 'deleteRestaurante'), 
]