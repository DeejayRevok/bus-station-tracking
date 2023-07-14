from bus_station.event_terminal.event_consumer_registry import EventConsumerRegistry
from yandil.container import default_container

from application.save_passenger_chain_node.command_tracking_created_consumer import CommandTrackingCreatedConsumer
from application.save_passenger_chain_node.event_tracking_created_consumer import EventTrackingCreatedConsumer


def register() -> None:
    registry = default_container[EventConsumerRegistry]

    event_consumers = [
        CommandTrackingCreatedConsumer,
        EventTrackingCreatedConsumer,
    ]
    for event_consumer in event_consumers:
        registry.register(default_container[event_consumer])
