from app.loaders.buses.event.events_mapping import map_events
from app.loaders.buses.event.threaded_event_bus_loader import load as load_threaded_event_bus


def load() -> None:
    map_events()
    load_threaded_event_bus()
