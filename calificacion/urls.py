from django.urls import path
from . import views

urlpatterns=[
    path('calificacion/list/',views.get_calificaciones, name= 'calificacionList'),
    path('calificacion/get/<int:id>/', views.get_calificacion, name= 'calificacion'), 
    path('calificacion/delete/<int:id>/', views.delete_calificacion, name= 'deleteCalificacion'), 
]