from datetime import datetime
from unittest import TestCase
from unittest.mock import Mock

from application.save_query_tracking.save_query_tracking_command import SaveQueryTrackingCommand
from application.save_query_tracking.save_query_tracking_command_handler import SaveQueryTrackingCommandHandler
from domain.query.query_tracking import QueryTracking
from domain.query.query_tracking_repository import QueryTrackingRepository


class TestSaveQueryTrackingCommandHandler(TestCase):
    def setUp(self) -> None:
        self.query_tracking_repository = Mock(spec=QueryTrackingRepository)
        self.command_handler = SaveQueryTrackingCommandHandler(query_tracking_repository=self.query_tracking_repository)

    def test_handle_non_existing_query_tracking(self):
        test_execution_start = datetime.now()
        test_execution_end = datetime.now()
        self.query_tracking_repository.find_by_id.return_value = None

        self.command_handler.handle(
            SaveQueryTrackingCommand(
                id="id",
                passenger_root_id="passenger_root_id",
                name="name",
                executor_name="executor_name",
                data={"data": "data"},
                execution_start=test_execution_start.isoformat(),
                execution_end=test_execution_end.isoformat(),
                success=True,
                response_data={"data": "data"},
            )
        )

        self.query_tracking_repository.save.assert_called_once_with(
            QueryTracking(
                id="id",
                root_passenger_id="passenger_root_id",
                name="name",
                executor_name="executor_name",
                data={"data": "data"},
                execution_start=test_execution_start,
                execution_end=test_execution_end,
                success=True,
                response_data={"data": "data"},
            )
        )

    def test_handle_non_existing_query_tracking_missing_execution_start(self):
        self.query_tracking_repository.find_by_id.return_value = None

        with self.assertRaises(Exception):
            self.command_handler.handle(
                SaveQueryTrackingCommand(
                    id="id",
                    passenger_root_id="passenger_root_id",
                    name="name",
                    executor_name="executor_name",
                    data={"data": "data"},
                    execution_start=None,
                    execution_end=None,
                    success=True,
                    response_data={"data": "data"},
                )
            )

    def test_handle_existing_query_tracking(self):
        test_execution_start = datetime.now()
        test_execution_end = datetime.now()
        self.query_tracking_repository.find_by_id.return_value = QueryTracking(
            id="id",
            root_passenger_id="passenger_root_id",
            name="name",
            executor_name="executor_name",
            data={"data": "data"},
            execution_start=test_execution_start,
            execution_end=None,
            success=None,
            response_data=None,
        )

        self.command_handler.handle(
            SaveQueryTrackingCommand(
                id="id",
                passenger_root_id="passenger_root_id",
                name="name",
                executor_name="executor_name",
                data={"data": "data"},
                execution_start=None,
                execution_end=test_execution_end.isoformat(),
                success=True,
                response_data={"data": "data"},
            )
        )

        self.query_tracking_repository.save.assert_called_once_with(
            QueryTracking(
                id="id",
                root_passenger_id="passenger_root_id",
                name="name",
                executor_name="executor_name",
                data={"data": "data"},
                execution_start=test_execution_start,
                execution_end=test_execution_end,
                success=True,
                response_data={"data": "data"},
            )
        )
