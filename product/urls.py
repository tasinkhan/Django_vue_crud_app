from django.urls import path, include
from . import views

urlpatterns = [
    path('api/products', views.product_list),
    path('api/products/<int:id>/', views.product_detail),
]