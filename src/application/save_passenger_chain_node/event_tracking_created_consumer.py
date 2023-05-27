from bus_station.command_terminal.bus.command_bus import CommandBus
from bus_station.event_terminal.event_consumer import EventConsumer

from application.save_passenger_chain_node.save_passenger_chain_node_command import SavePassengerChainNodeCommand
from domain.event.event_tracking_created_event import EventTrackingCreatedEvent
from domain.passenger.chain.passenger_chain_node_type import PassengerChainNodeType


class EventTrackingCreatedConsumer(EventConsumer):
    def __init__(
        self,
        command_bus: CommandBus,
    ):
        self.__command_bus = command_bus

    def consume(self, event: EventTrackingCreatedEvent) -> None:
        save_passenger_chain_node_command = SavePassengerChainNodeCommand(
            id=event.id,
            name=event.name,
            node_root_passenger_id=event.tracking_root_passenger_id,
            type=PassengerChainNodeType.EVENT.value,
        )
        self.__command_bus.transport(save_passenger_chain_node_command)
