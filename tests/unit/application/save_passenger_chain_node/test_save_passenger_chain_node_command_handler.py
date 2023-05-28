from unittest import TestCase
from unittest.mock import Mock

from application.save_passenger_chain_node.save_passenger_chain_node_command import SavePassengerChainNodeCommand
from application.save_passenger_chain_node.save_passenger_chain_node_command_handler import (
    SavePassengerChainNodeCommandHandler,
)
from domain.passenger.chain.passenger_chain_node import PassengerChainNode
from domain.passenger.chain.passenger_chain_node_repository import PassengerChainNodeRepository
from domain.passenger.chain.passenger_chain_node_type import PassengerChainNodeType


class TestSavePassengerChainNodeCommandHandler(TestCase):
    def setUp(self) -> None:
        self.passenger_chain_node_repository = Mock(spec=PassengerChainNodeRepository)
        self.save_passenger_chain_node_command_handler = SavePassengerChainNodeCommandHandler(
            passenger_chain_node_repository=self.passenger_chain_node_repository
        )

    def test_handle(self):
        self.save_passenger_chain_node_command_handler.handle(
            command=SavePassengerChainNodeCommand(
                id="id",
                name="name",
                node_root_passenger_id="root_passenger_id",
                type="command",
            )
        )
        self.passenger_chain_node_repository.save.assert_called_once_with(
            PassengerChainNode(
                id="id",
                name="name",
                root_passenger_id="root_passenger_id",
                type=PassengerChainNodeType.COMMAND,
            )
        )
