from django.http import JsonResponse
from .services import get_events

def get_events_view(request):
    """
    View function to fetch events within the specified time range and return them as a JSON response.

    Parameters:
        request (HttpRequest): The request object containing 'starts_at' and 'ends_at' parameters.

    Returns:
        JsonResponse: A JSON response containing the list of events.

    Raises:
        ValueError: If 'starts_at' or 'ends_at' parameters are not provided.
    """
    return get_events(request)
