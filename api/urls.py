from django.urls import path
from . import views

urlpatterns = [
    path('ping/', views.ping, name='ping'),

    path('products/', views.products_list, name='products_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),

    path('categories/', views.categories_list, name='categories_list'),
    path('filters/', views.filters, name='filters'),

    path('orders/', views.create_order, name='create_order'),
    path('feedback/', views.create_feedback, name='create_feedback'),
]