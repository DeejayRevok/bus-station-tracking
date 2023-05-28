from unittest import TestCase
from unittest.mock import Mock, patch
from uuid import uuid4

from bus_station.command_terminal.bus.command_bus import CommandBus
from freezegun import freeze_time

from application.save_passenger_chain_node.command_tracking_created_consumer import CommandTrackingCreatedConsumer
from application.save_passenger_chain_node.save_passenger_chain_node_command import SavePassengerChainNodeCommand
from domain.command.command_tracking_created_event import CommandTrackingCreatedEvent


@patch("bus_station.passengers.passenger.uuid4", return_value=str(uuid4()))
@freeze_time()
class TestCommandTrackingCreatedConsumer(TestCase):
    def setUp(self) -> None:
        self.command_bus = Mock(spec=CommandBus)
        self.command_tracking_created_consumer = CommandTrackingCreatedConsumer(
            command_bus=self.command_bus,
        )

    def test_consume(self, *_):
        self.command_tracking_created_consumer.consume(
            event=CommandTrackingCreatedEvent(
                id="id",
                name="name",
                tracking_root_passenger_id="tracking_root_passenger_id",
                data={"data": "data"},
                executor_name="executor_name",
            )
        )

        self.command_bus.transport.assert_called_once_with(
            SavePassengerChainNodeCommand(
                id="id",
                name="name",
                node_root_passenger_id="tracking_root_passenger_id",
                type="command",
            )
        )
