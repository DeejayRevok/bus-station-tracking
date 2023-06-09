from bus_station.command_terminal.command_handler_registry import CommandHandlerRegistry
from yandil.container import default_container


def register() -> None:
    registry = default_container[CommandHandlerRegistry]

    command_handler_fqns = [
        "application.save_command_tracking.save_command_tracking_command_handler.SaveCommandTrackingCommandHandler",
        "application.save_event_tracking.save_event_tracking_command_handler.SaveEventTrackingCommandHandler",
        "application.save_query_tracking.save_query_tracking_command_handler.SaveQueryTrackingCommandHandler",
        "application.save_passenger_chain_node"
        ".save_passenger_chain_node_command_handler.SavePassengerChainNodeCommandHandler",
    ]
    for command_handler_fqn in command_handler_fqns:
        registry.register(command_handler_fqn)
