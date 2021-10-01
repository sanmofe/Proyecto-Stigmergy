from django.urls import path
from . import views

urlpatterns=[
    path('restaurante/list/',views.get_resturantes, name= 'restauranteList'),
    path('restaurante/get/<int:id>/', views.get_resturante, name= 'restaurante'),
    path('restaurante/delete/<int:id>/', views.delete_resturante, name= 'deleteRestaurante'), 
]
