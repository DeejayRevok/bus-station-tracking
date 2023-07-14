from bus_station.command_terminal.command_handler_registry import CommandHandlerRegistry
from yandil.container import default_container

from application.save_command_tracking.save_command_tracking_command_handler import SaveCommandTrackingCommandHandler
from application.save_event_tracking.save_event_tracking_command_handler import SaveEventTrackingCommandHandler
from application.save_passenger_chain_node.save_passenger_chain_node_command_handler import \
    SavePassengerChainNodeCommandHandler
from application.save_query_tracking.save_query_tracking_command_handler import SaveQueryTrackingCommandHandler


def register() -> None:
    registry = default_container[CommandHandlerRegistry]

    command_handlers = [
        SaveCommandTrackingCommandHandler,
        SaveEventTrackingCommandHandler,
        SaveQueryTrackingCommandHandler,
        SavePassengerChainNodeCommandHandler,
    ]
    for command_handler in command_handlers:
        registry.register(default_container[command_handler])
