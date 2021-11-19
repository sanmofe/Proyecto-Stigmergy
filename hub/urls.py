
from django.urls import path
from . import views

urlpatterns = [
    path('create/'  ,views.create_comprador    ,name='createComprador')
]