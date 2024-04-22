import requests
import xml.etree.ElementTree as ET

# Global variable for caching
event_cache = []

def fetch_events(starts_at, ends_at, include_past=False):

    """
    Fetches events within the specified time range and returns them.

    Parameters:
        starts_at (str): The start date and time of the range.
        ends_at (str): The end date and time of the range.
        include_past (bool, optional): Whether to include past events. Defaults to False.

    Returns:
        list: A list of events within the specified time range.

    """
    global event_cache

    # Check if there are cached events and return them if the provider service is down
    if not event_cache:
        try:
            # Attempt to fetch events from the provider
            response = requests.get("https://provider.code-challenge.feverup.com/api/events")
            response.raise_for_status()
            root = ET.fromstring(response.content)

            # Parse and extend the event cache with the newly fetched events
            event_cache.extend(parse_events(root))
        except requests.RequestException as e:
            # In case of a failed request, return the cached events
            print(f"Failed to fetch events from provider: {e}")
            return event_cache if event_cache else []
        except ET.ParseError as e:
            # Error handling for XML parsing error
            print(f"Failed to parse XML content: {e}")
            return event_cache if event_cache else []

    # Filter events based on the specified time range
    events = []
    for event in event_cache:
        # Check if the event falls within the specified time range
        if include_past or (starts_at <= event['start_date'] <= ends_at):
            events.append(event)
    return events

def parse_events(root):
    """
    Parse the XML data and extract event information.

    Args:
        root (ElementTree.Element): The root element of the XML tree.

    Returns:
        list: A list of dictionaries containing event details.

    """
    events = []
    # Iterate through each 'event' element in the XML tree
    for event_elem in root.findall('.//event'):

        # Find the 'title' element
        title_elem = event_elem.find('.//title')

        # Extract the title if available, otherwise None
        title = title_elem.text if title_elem is not None else None

         # Create a dictionary to store the event details
        event = {
            'id': event_elem.get('event_id'), # Extracting the event ID
            'title': title, # Extracting the event title
            'start_date': event_elem.get('event_start_date'),  # Extracting the event start date
            'start_time': event_elem.get('event_start_time'),  # Extracting the event start time
            'end_date': event_elem.get('event_end_date'),  # Extracting the event end date
            'end_time': event_elem.get('event_end_time'),  # Extracting the event end time
            'min_price': float(event_elem.find('.//zone').get('price')),  # Extracting the minimum price
            'max_price': float(event_elem.find('.//zone').get('price'))  # Extracting the maximum price
        } 

        # Append the event details dictionary to the list of events
        events.append(event)
    return events
