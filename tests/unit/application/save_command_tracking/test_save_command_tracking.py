from datetime import datetime
from unittest import TestCase
from unittest.mock import Mock

from bus_station.event_terminal.bus.event_bus import EventBus

from application.save_command_tracking.save_command_tracking_command import SaveCommandTrackingCommand
from application.save_command_tracking.save_command_tracking_command_handler import SaveCommandTrackingCommandHandler
from domain.command.command_tracking import CommandTracking
from domain.command.command_tracking_created_event import CommandTrackingCreatedEvent
from domain.command.command_tracking_repository import CommandTrackingRepository


class TestSaveCommandTracking(TestCase):
    def setUp(self) -> None:
        self.command_tracking_repository = Mock(spec=CommandTrackingRepository)
        self.event_bus = Mock(spec=EventBus)
        self.command_handler = SaveCommandTrackingCommandHandler(
            command_tracking_repository=self.command_tracking_repository, event_bus=self.event_bus
        )

    def test_handle_non_existing_command_tracking(self):
        test_execution_start = datetime.now()
        test_execution_end = datetime.now()
        self.command_tracking_repository.find_by_id.return_value = None

        self.command_handler.handle(
            SaveCommandTrackingCommand(
                id="id",
                passenger_root_id="passenger_root_id",
                name="name",
                executor_name="executor_name",
                data={"data": "data"},
                execution_start=test_execution_start.isoformat(),
                execution_end=test_execution_end.isoformat(),
                success=True,
            )
        )

        self.command_tracking_repository.save.assert_called_once_with(
            CommandTracking(
                id="id",
                root_passenger_id="passenger_root_id",
                name="name",
                executor_name="executor_name",
                data={"data": "data"},
                execution_start=test_execution_start,
                execution_end=test_execution_end,
                success=True,
            )
        )
        self.event_bus.transport.assert_called_once_with(
            CommandTrackingCreatedEvent(
                id="id",
                tracking_root_passenger_id="passenger_root_id",
                name="name",
                executor_name="executor_name",
                data={"data": "data"},
            )
        )

    def test_handle_non_existing_command_tracking_missing_execution_start(self):
        self.command_tracking_repository.find_by_id.return_value = None

        with self.assertRaises(Exception):
            self.command_handler.handle(
                SaveCommandTrackingCommand(
                    id="id",
                    passenger_root_id="passenger_root_id",
                    name="name",
                    executor_name="executor_name",
                    data={"data": "data"},
                    execution_start=None,
                    execution_end=None,
                    success=True,
                )
            )
        self.event_bus.transport.assert_not_called()

    def test_handle_existing_command_tracking(self):
        test_execution_start = datetime.now()
        test_execution_end = datetime.now()
        self.command_tracking_repository.find_by_id.return_value = CommandTracking(
            id="id",
            root_passenger_id="passenger_root_id",
            name="name",
            executor_name="executor_name",
            data={"data": "data"},
            execution_start=test_execution_start,
            execution_end=None,
            success=None,
        )

        self.command_handler.handle(
            SaveCommandTrackingCommand(
                id="id",
                passenger_root_id="passenger_root_id",
                name="name",
                executor_name="executor_name",
                data={"data": "data"},
                execution_start=None,
                execution_end=test_execution_end.isoformat(),
                success=True,
            )
        )

        self.command_tracking_repository.save.assert_called_once_with(
            CommandTracking(
                id="id",
                root_passenger_id="passenger_root_id",
                name="name",
                executor_name="executor_name",
                data={"data": "data"},
                execution_start=test_execution_start,
                execution_end=test_execution_end,
                success=True,
            )
        )
        self.event_bus.transport.assert_not_called()
