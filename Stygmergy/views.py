# -*- coding: utf-8 -*-
"""
Created on Fri Oct 1 02:47:02 2021

@author: Miguel
"""

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
