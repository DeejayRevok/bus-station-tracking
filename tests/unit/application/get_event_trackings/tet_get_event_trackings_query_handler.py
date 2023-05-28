from unittest import TestCase
from unittest.mock import Mock

from application.get_event_trackings.get_event_trackings_query import GetEventTrackingsQuery
from application.get_event_trackings.get_event_trackings_query_handler import GetEventTrackingsQueryHandler
from domain.event.event_tracking import EventTracking
from domain.event.event_tracking_repository import EventTrackingRepository
from domain.passenger.find_passenger_tracking_criteria import FindPassengerTrackingCriteria


class TestGetEventTrackingsQueryHandler(TestCase):
    def setUp(self) -> None:
        self.event_tracking_repository = Mock(spec=EventTrackingRepository)
        self.get_event_trackings_query_handler = GetEventTrackingsQueryHandler(
            event_tracking_repository=self.event_tracking_repository
        )

    def test_handle(self) -> None:
        test_return_event_trackings = [
            EventTracking(
                id="test_event_id",
                root_passenger_id="test_root_passenger_id",
                name="test_name",
                executor_name="test_executor_name",
                execution_start=None,
                execution_end=None,
                success=True,
                data={},
            ),
        ]
        self.event_tracking_repository.find_by_criteria.return_value = test_return_event_trackings

        response = self.get_event_trackings_query_handler.handle(GetEventTrackingsQuery())

        self.assertEqual(response.data, test_return_event_trackings)
        self.event_tracking_repository.find_by_criteria.assert_called_once_with(FindPassengerTrackingCriteria())
