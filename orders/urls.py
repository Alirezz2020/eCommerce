from django.urls import path
from . import views

app_name = 'orders'

urlpatterns=[
    path('cart/', views.CartView.as_view(), name='cart'),
    path('cart/add/<int:product_id>/', views.CartAddView.as_view(), name='cart_add'),
    path('cart/remove/<int:product_id>/', views.CartRemoveView.as_view(), name='cart_remove'),
    path('create/', views.OrderCreateView.as_view(), name='orders_create'),
    path('detail/<int:product_id>/', views.OrderDetailView.as_view(), name='orders_detail'),
]