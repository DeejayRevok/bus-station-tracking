from app.loaders.buses.command import load as load_command_bus
from app.loaders.buses.event import load as load_event_bus
from app.loaders.buses.query import load as load_query_bus


def load() -> None:
    load_command_bus()
    load_query_bus()
    load_event_bus()
