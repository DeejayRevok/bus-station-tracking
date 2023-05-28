from unittest import TestCase
from unittest.mock import Mock

from application.get_command_trackings.get_command_trackings_query import GetCommandTrackingsQuery
from application.get_command_trackings.get_command_trackings_query_handler import GetCommandTrackingsQueryHandler
from domain.command.command_tracking import CommandTracking
from domain.command.command_tracking_repository import CommandTrackingRepository
from domain.passenger.find_passenger_tracking_criteria import FindPassengerTrackingCriteria


class TestGetCommandTrackingsQueryHandler(TestCase):
    def setUp(self) -> None:
        self.command_tracking_repository = Mock(spec=CommandTrackingRepository)
        self.get_command_trackings_query_handler = GetCommandTrackingsQueryHandler(
            command_tracking_repository=self.command_tracking_repository
        )

    def test_handle(self) -> None:
        test_return_command_trackings = [
            CommandTracking(
                id="test_command_id",
                root_passenger_id="test_root_passenger_id",
                name="test_name",
                executor_name="test_executor_name",
                execution_start=None,
                execution_end=None,
                success=True,
                data={},
            ),
        ]
        self.command_tracking_repository.find_by_criteria.return_value = test_return_command_trackings

        response = self.get_command_trackings_query_handler.handle(GetCommandTrackingsQuery())

        self.assertEqual(response.data, test_return_command_trackings)
        self.command_tracking_repository.find_by_criteria.assert_called_once_with(FindPassengerTrackingCriteria())
