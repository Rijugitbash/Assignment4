import datetime
# from datetime import timedelta

def calculate_on_time_delivery_percentage(delivery_data):
    on_time_count = 0

    for order in delivery_data:
        delivery_datetime = order.get('delivery_date')
        acknowledgment_datetime = order.get('acknowledgment_date')

        if delivery_datetime and acknowledgment_datetime:
            if acknowledgment_datetime <= delivery_datetime:
                on_time_count += 1

    total_orders = len(delivery_data)
    
    if total_orders == 0:
        return 0  

    on_time_percentage = (on_time_count / total_orders) * 100
    return on_time_percentage

def calculate_average_rating(vendor_all_order):
    total_ratings = 0

    for rating_dict in vendor_all_order:
        rating = rating_dict.get('quality_rating')

        if rating is not None:  # Check if rating exists and is not None
            total_ratings += rating

    num_ratings = len(vendor_all_order)

    if num_ratings == 0:
        return 0 
    average_rating = total_ratings / num_ratings
    return average_rating

def calculate_completion_percentage(vendor_all_order):
    completed_count = 0

    for po_dict in vendor_all_order:
        status = po_dict.get('status')

        if status == 'completed':
            completed_count += 1

    total_pos = len(vendor_all_order)
    
    if total_pos == 0:
        return 0 
    completion_percentage = (completed_count / total_pos) * 100
    return completion_percentage

def calculate_average_response_time(vendor_all_order):
    total_response_time = 0
    num_pos = 0

    for po_dict in vendor_all_order:
        issue_date_str = po_dict.get('issue_date')
        acknowledgment_date_str = po_dict.get('acknowledgment_date')

        if issue_date_str and acknowledgment_date_str:
            time_difference = issue_date_str - acknowledgment_date_str
            total_response_time += time_difference.total_seconds()
            num_pos += 1

    if num_pos == 0:
        return 0  # Avoid division by zero if the list is empty

    # Calculate the average response time in days
    average_response_time_seconds = total_response_time / num_pos
    average_response_time_days = average_response_time_seconds / (24 * 3600)  # 24 hours * 3600 seconds
    return average_response_time_days
