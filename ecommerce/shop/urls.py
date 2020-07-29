from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='shop'),
    path('about/', views.about, name ='About'),
    path('contact/', views.contact, name ='Contact'),
    path('tracker/', views.tracker, name ='Tracker'),
    path('checkout/', views.checkout, name ='Checkout'),
    path('products/<int:myid>', views.productView, name ='ProductView'),
    path('search/', views.search, name ='Search'),
    # path('', views.index, name ='shop'),
    # path('', views.index, name ='shop'),
]