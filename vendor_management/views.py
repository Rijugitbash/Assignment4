from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from .calculate_logic import *


# Vendor Views
@api_view(['GET', 'POST'])
def vendor_list_create(request):
    if request.method == 'GET':
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            vendor_obj = serializer.save()
            HistoricalPerformance.objects.create(vendor_id = vendor_obj.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def vendor_detail(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)

    if request.method == 'GET':
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def VendorFilterView(request):
    queryset = Vendor.objects.all()
    serializer = VendorSerializer(queryset, many=True)
    vendor_filter = VendorFilter(request.GET, queryset=queryset)
    serializer = VendorSerializer(vendor_filter.qs, many=True)
    return Response(serializer.data)

# Purchase Order Views
@api_view(['GET', 'POST'])
def purchase_order_list_create(request):
    if request.method == 'GET':
        purchase_orders = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(purchase_orders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PurchaseOrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def purchase_order_detail(request, pk):
    purchase_order = get_object_or_404(PurchaseOrder, pk=pk)

    if request.method == 'GET':
        serializer = PurchaseOrderSerializer(purchase_order)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PurchaseOrderSerializer(purchase_order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        purchase_order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET','POST'])
def after_complate_order(request, pk):
    if request.method == "GET":
        purchase_order = get_object_or_404(PurchaseOrder, pk=pk)
        return Response({"Status":purchase_order.status, "Rating": purchase_order.quality_rating})
    
    if request.method == "POST":
        quality_rating = request.data.get("quality_rating")  # Change () to .get()
        purchase_order = get_object_or_404(PurchaseOrder, pk=pk)
        purchase_order_details = PurchaseOrder.objects.filter(id=pk).first()
        purchase_order_details.status = "completed"
        purchase_order_details.quality_rating = float(quality_rating)
        purchase_order_details.acknowledgment_date = datetime.datetime.now()
        purchase_order_details.save()

        vendor_all_order = PurchaseOrder.objects.filter(vendor_id=purchase_order.vendor, status="completed").values()  
        on_time_delivery_percentage = calculate_on_time_delivery_percentage(vendor_all_order)
        average_rating = calculate_average_rating(vendor_all_order)
        average_response_time = calculate_average_response_time(vendor_all_order)
        completion_percentage = calculate_completion_percentage(vendor_all_order)
        print(on_time_delivery_percentage, average_rating, average_response_time, completion_percentage)
        Vendor.objects.filter(id=purchase_order.vendor.id).update(
            on_time_delivery_rate=float(on_time_delivery_percentage),
            quality_rating_avg=float(average_rating),
            average_response_time=float(average_response_time),
            fulfillment_rate=float(completion_percentage)
        )
        vendor_history = HistoricalPerformance.objects.filter(vendor_id=purchase_order.vendor).first()
        vendor_history.date = datetime.datetime.now()
        vendor_history.on_time_delivery_rate = float(on_time_delivery_percentage)
        vendor_history.quality_rating_avg = float(average_rating)
        vendor_history.average_response_time = float(average_response_time)
        vendor_history.fulfillment_rate = float(completion_percentage)
        vendor_history.save()
    return Response({"res": "Delivery Successfully completed"})


# Vendor Performance View
@api_view(['GET'])
def vendor_performance(request, pk):
    vendor = get_object_or_404(Vendor, pk=pk)
    performance = HistoricalPerformance.objects.filter(vendor=vendor).latest('date')
    serializer = HistoricalPerformanceSerializer(performance)
    return Response(serializer.data)
