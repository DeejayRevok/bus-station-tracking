from bus_station.event_terminal.event import Event
from bus_station.passengers.passenger_mapper import passenger_mapper

from domain.command.command_tracking_created_event import CommandTrackingCreatedEvent
from domain.event.event_tracking_created_event import EventTrackingCreatedEvent


def map_events() -> None:
    passenger_mapper(CommandTrackingCreatedEvent, Event)
    passenger_mapper(EventTrackingCreatedEvent, Event)
