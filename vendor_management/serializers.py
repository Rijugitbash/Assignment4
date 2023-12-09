from rest_framework import serializers
from .models import *

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'name', 'contact_details', 'address', 'vendor_code']

class PurchaseOrderSerializer(serializers.ModelSerializer):
    vendor = VendorSerializer()

    class Meta:
        model = PurchaseOrder
        fields = ['id', 'po_number', 'vendor', 'order_date', 'items', 'quantity', 'status']
        read_only_fields = ['id']


class VendorPerfomanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'name', 'contact_details', 'address', 'vendor_code', 'on_time_delivery_rate',
                  'quality_rating_avg', 'average_response_time', 'fulfillment_rate']
        read_only_fields = ['id']
