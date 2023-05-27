from bus_station.event_terminal.event_consumer_registry import EventConsumerRegistry
from pypendency.builder import container_builder


def register() -> None:
    registry: EventConsumerRegistry = container_builder.get(
        "bus_station.event_terminal.event_consumer_registry.EventConsumerRegistry"
    )

    command_handler_fqns = [
        "application.save_passenger_chain_node.command_tracking_created_consumer.CommandTrackingCreatedConsumer",
        "application.save_passenger_chain_node.event_tracking_created_consumer.EventTrackingCreatedConsumer",
    ]
    for command_handler_fqn in command_handler_fqns:
        registry.register(command_handler_fqn)
