from django.urls import path
from . import views

urlpatterns=[
    path('comprador/list/',views.get_compradores, name= 'compradorList'),
    path('comprador/get/<int:id>/', views.get_comprador, name= 'comprador'), 
    path('comprador/delete/<int:id>/', views.delete_comprador, name= 'deleteComprador'),
    path('comprador/create',views.create_comprador, name='createComprador') 
]