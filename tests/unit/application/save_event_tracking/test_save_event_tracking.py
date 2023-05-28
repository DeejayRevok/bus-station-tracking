from datetime import datetime
from unittest import TestCase
from unittest.mock import Mock

from bus_station.event_terminal.bus.event_bus import EventBus

from application.save_event_tracking.save_event_tracking_command import SaveEventTrackingCommand
from application.save_event_tracking.save_event_tracking_command_handler import SaveEventTrackingCommandHandler
from domain.event.event_tracking import EventTracking
from domain.event.event_tracking_created_event import EventTrackingCreatedEvent
from domain.event.event_tracking_repository import EventTrackingRepository


class TestSaveEventTracking(TestCase):
    def setUp(self) -> None:
        self.event_tracking_repository = Mock(spec=EventTrackingRepository)
        self.event_bus = Mock(spec=EventBus)
        self.event_handler = SaveEventTrackingCommandHandler(
            event_tracking_repository=self.event_tracking_repository, event_bus=self.event_bus
        )

    def test_handle_non_existing_event_tracking(self, *_):
        test_execution_start = datetime.now()
        test_execution_end = datetime.now()
        self.event_tracking_repository.find_by_id.return_value = None

        self.event_handler.handle(
            SaveEventTrackingCommand(
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

        self.event_tracking_repository.save.assert_called_once_with(
            EventTracking(
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
            EventTrackingCreatedEvent(
                id="id",
                tracking_root_passenger_id="passenger_root_id",
                name="name",
                executor_name="executor_name",
                data={"data": "data"},
            )
        )

    def test_handle_non_existing_event_tracking_missing_execution_start(self, *_):
        self.event_tracking_repository.find_by_id.return_value = None

        with self.assertRaises(Exception):
            self.event_handler.handle(
                SaveEventTrackingCommand(
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

    def test_handle_existing_event_tracking(self, *_):
        test_execution_start = datetime.now()
        test_execution_end = datetime.now()
        self.event_tracking_repository.find_by_id.return_value = EventTracking(
            id="id",
            root_passenger_id="passenger_root_id",
            name="name",
            executor_name="executor_name",
            data={"data": "data"},
            execution_start=test_execution_start,
            execution_end=None,
            success=None,
        )

        self.event_handler.handle(
            SaveEventTrackingCommand(
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

        self.event_tracking_repository.save.assert_called_once_with(
            EventTracking(
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
