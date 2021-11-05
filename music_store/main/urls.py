from django.urls import path
from .views import ProductDetailView, \
    BaseView, \
    CategoryDetailView, \
    CartView, \
    AddToCartView, \
    DeleteFromCartView, \
    ChangeQTYView, \
    CheckoutView, \
    MakeOrderView, \
    LoginView


urlpatterns = [
    path('', BaseView.as_view(), name = 'base'),
    path('products/<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add_to_cart/<str:ct_model>/<str:slug>/', AddToCartView.as_view(), name='add_to_cart'),
    path('delete_from_cart/<str:ct_model>/<str:slug>/', DeleteFromCartView.as_view(), name='delete_from_cart'),
    path('change_qty_cart/<str:ct_model>/<str:slug>/', ChangeQTYView.as_view(), name='change_qty_cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('make_order/', MakeOrderView.as_view(), name='make_order'),
    path('login/', LoginView.as_view(), name='login'),
]