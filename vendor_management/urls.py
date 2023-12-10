from django.urls import path
from .views import *

urlpatterns = [
    path('api/vendors/', vendor_list_create, name='vendor-list-create'),
    path('api/vendors/<int:pk>/', vendor_detail, name='vendor-detail'),
    path('api/purchase_orders/', purchase_order_list_create, name='purchase-order-list-create'),
    path('api/purchase_orders/<int:pk>/', purchase_order_detail, name='purchase-order-detail'),

    path('api/order_complete/<int:pk>', after_complate_order, name='vendor-performance'),

    path('api/vendors/<int:pk>/performance/', vendor_performance, name='vendor-performance'),

    path('vendors/', VendorFilterView, name='vendor-list'),
]