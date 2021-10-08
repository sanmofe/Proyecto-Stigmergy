# -*- coding: utf-8 -*-
"""
Created on Fri Oct 1 02:02:02 2021

@author: Miguel
"""

from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.list_pedido,name='list_pedido')
]
