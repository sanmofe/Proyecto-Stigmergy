from django.urls import path
from . import views

urlpatterns=[
    path('list/',views.list_productos, name= 'productoList'),
    path('get/<int:id>/', views.get_producto, name= 'producto'), 
    path('delete/<int:id>/', views.delete_producto, name= 'deleteProducto'),
    path('update/<int:id>/<int:idPedido>', views.update_producto, name= 'updateProducto')
]