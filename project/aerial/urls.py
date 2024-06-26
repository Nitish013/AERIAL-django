from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('features/', views.features, name='features'),
    path('price/', views.price, name='price'),
    path('teams/', views.contact, name='contact'),
    path('create/', views.create, name='create'),
    path('retrieve/', views.retrieve, name='retrieve'),
    path('update/<did>', views.update),
    path('delete/<sid>', views.delete),
]