import requests
import xml.etree.ElementTree as ET

# Global variable for caching
event_cache = []

def fetch_events(starts_at, ends_at, include_past=False):
    global event_cache

    # Check if there are cached events and return them if the provider service is down
    if not event_cache:
        try:
            response = requests.get("https://provider.code-challenge.feverup.com/api/events")
            response.raise_for_status()
            root = ET.fromstring(response.content)
            event_cache.extend(parse_events(root))
        except requests.RequestException as e:
            print(f"Failed to fetch events from provider: {e}")
            return event_cache if event_cache else []

    # Filter events based on the specified time range
    events = []
    for event in event_cache:
        if include_past or (starts_at <= event['start_date'] <= ends_at):
            events.append(event)
    return events

def parse_events(root):
    events = []
    for event_elem in root.findall('.//event'):
        title_elem = event_elem.find('.//title')
        title = title_elem.text if title_elem is not None else None
        event = {
            'id': event_elem.get('event_id'),
            'title': title,
            'start_date': event_elem.get('event_start_date'),
            'start_time': event_elem.get('event_start_time'),
            'end_date': event_elem.get('event_end_date'),
            'end_time': event_elem.get('event_end_time'),
            'min_price': float(event_elem.find('.//zone').get('price')),
            'max_price': float(event_elem.find('.//zone').get('price'))
        }
        events.append(event)
    return events
