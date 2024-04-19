from django.http import JsonResponse
from .models import Event
from .utils import fetch_events

def get_events(request):
   # Retrieve starts_at and ends_at parameters from the request
    starts_at = request.GET.get('starts_at')
    ends_at = request.GET.get('ends_at')

    # Check if starts_at and ends_at parameters are provided
    if starts_at is None or ends_at is None:
        return JsonResponse({"error": "Both 'starts_at' and 'ends_at' parameters are required."}, status=400)

    # Call fetch_events function with starts_at and ends_at parameters
    events_data = fetch_events(starts_at, ends_at)


    # Process events data and save it to database
    for event_data in events_data:
        event = Event(
            id=event_data["id"],
            title=event_data["title"],
            start_date=event_data["start_date"],
            start_time=event_data["start_time"],
            end_date=event_data["end_date"],
            end_time=event_data["end_time"],
            min_price=event_data["min_price"],
            max_price=event_data["max_price"]
        )
        #event.save()

    # Retrieve events within the specified time range as provided
    starts_at = request.GET.get('starts_at')
    ends_at = request.GET.get('ends_at')

    if starts_at is None or ends_at is None:
        return JsonResponse({"error": "Both 'starts_at' and 'ends_at' parameters are required."}, status=400)

    start_date, end_date = starts_at.split('T')[0], ends_at.split('T')[0]
    start_time, end_time = starts_at.split('T')[1], ends_at.split('T')[1]

    events = Event.objects.filter(start_date__lte=end_date, end_date__gte=start_date, start_time__lte=end_time, end_time__gte=start_time).values()
    return JsonResponse({"events": events_data})