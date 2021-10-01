from django.urls import path
from . import views

urlpatterns=[
    path('producto/list/',views.get_productos, name= 'productoList'),
    path('producto/get/<int:id>/', views.get_producto, name= 'producto'), 
    path('producto/delete/<int:id>/', views.delete_producto, name= 'deleteProducto')
]