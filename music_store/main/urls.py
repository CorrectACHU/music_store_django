from django.urls import path
from .views import ProductDetailView, BaseView, CategoryDetailView, CartView, AddToCartView


urlpatterns = [
    path('', BaseView.as_view(), name = 'base'),
    path('products/<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add_to_cart/<str:ct_model>/<str:slug>/', AddToCartView.as_view(), name='add_to_cart'),
]