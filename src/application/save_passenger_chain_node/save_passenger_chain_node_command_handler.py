from bus_station.command_terminal.command_handler import CommandHandler

from application.save_passenger_chain_node.save_passenger_chain_node_command import SavePassengerChainNodeCommand
from domain.passenger.chain.passenger_chain_node import PassengerChainNode
from domain.passenger.chain.passenger_chain_node_repository import PassengerChainNodeRepository
from domain.passenger.chain.passenger_chain_node_type import PassengerChainNodeType


class SavePassengerChainNodeCommandHandler(CommandHandler):
    def __init__(self, passenger_chain_node_repository: PassengerChainNodeRepository):
        self.__passenger_chain_node_repository = passenger_chain_node_repository

    def handle(self, command: SavePassengerChainNodeCommand) -> None:
        passenger_chain_node = PassengerChainNode(
            id=command.id,
            name=command.name,
            root_passenger_id=command.node_root_passenger_id,
            type=PassengerChainNodeType(command.type),
        )
        self.__passenger_chain_node_repository.save(passenger_chain_node)
