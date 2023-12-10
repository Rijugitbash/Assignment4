from rest_framework import serializers
from .models import *
import django_filters

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ["name","contact_details","address","vendor_code"]

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

class HistoricalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = '__all__'

# filters.py
import django_filters
from .models import Vendor

class VendorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    contact_details = django_filters.CharFilter(lookup_expr='icontains')
    address = django_filters.CharFilter(lookup_expr='icontains')
    vendor_code = django_filters.CharFilter(lookup_expr='icontains')
    on_time_delivery_rate = django_filters.NumberFilter()
    quality_rating_avg = django_filters.NumberFilter()
    average_response_time = django_filters.NumberFilter()
    fulfillment_rate = django_filters.NumberFilter()

    class Meta:
        model = Vendor
        fields = {
            'name': ['icontains'],
            'contact_details': ['icontains'],
            'address': ['icontains'],
            'vendor_code': ['icontains'],
            'on_time_delivery_rate': ['exact', 'gte', 'lte'],
            'quality_rating_avg': ['exact', 'gte', 'lte'],
            'average_response_time': ['exact', 'gte', 'lte'],
            'fulfillment_rate': ['exact', 'gte', 'lte'],
        }

