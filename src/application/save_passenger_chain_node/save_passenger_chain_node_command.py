from dataclasses import dataclass

from bus_station.command_terminal.command import Command


@dataclass(frozen=True)
class SavePassengerChainNodeCommand(Command):
    id: str
    name: str
    node_root_passenger_id: str
    type: str
