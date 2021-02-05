from django.urls import path, include

import basketapp.views as basketapp

app_name = 'basketapp'

# Сделал на будущее
urlpatterns = [
    path('', basketapp.basket, name='view'),
    path('add/<int:pk>/', basketapp.add, name='add'),
    path('delete/<int:pk>/', basketapp.remove, name='remove'),
    path('edit/<int:pk>/<int:quantity>/', basketapp.basket_edit, name='edit'),
]