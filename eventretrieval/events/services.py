from django.http import JsonResponse
from .models import Event
from .utils import fetch_events

def get_events(request):
    """
    Fetches events within the specified time range and returns them as a JSON response.

    Parameters:
        request (HttpRequest): The request object containing 'starts_at' and 'ends_at' parameters.

    Returns:
        JsonResponse: A JSON response containing the list of events.

    Raises:
        ValueError: If 'starts_at' or 'ends_at' parameters are not provided.
    """
    # Retrieve starts_at and ends_at parameters from the request
    starts_at = request.GET.get('starts_at')
    ends_at = request.GET.get('ends_at')

    # Check if starts_at and ends_at parameters are provided
    if starts_at is None or ends_at is None:
        return JsonResponse({"error": "Both 'starts_at' and 'ends_at' parameters are required."}, status=400)

    try:
        # Call fetch_events function with starts_at and ends_at parameters
        events_data = fetch_events(starts_at, ends_at)
    except Exception as e:
        return JsonResponse({"error": f"Failed to fetch events: {e}"}, status=500)

    # Process events data and save it to the database
    for event_data in events_data:
        # Create Event object
        event = Event(
            id=event_data["id"],  # Event ID
            title=event_data["title"],  # Event title
            start_date=event_data["start_date"],  # Event start date
            start_time=event_data["start_time"],  # Event start time
            end_date=event_data["end_date"],  # Event end date
            end_time=event_data["end_time"],  # Event end time
            min_price=event_data["min_price"],  # Minimum price
            max_price=event_data["max_price"]  # Maximum price
        )

    # Retrieve events within the specified time range as provided
    # Split the provided dates and times
    start_date, end_date = starts_at.split('T')[0], ends_at.split('T')[0]
    start_time, end_time = starts_at.split('T')[1], ends_at.split('T')[1]

    # Retrieve events from the database within the specified time range
    events = Event.objects.filter(start_date__lte=end_date, end_date__gte=start_date, start_time__lte=end_time, end_time__gte=start_time).values()

    # Return the retrieved events as JSON response
    return JsonResponse({"events": events_data})
