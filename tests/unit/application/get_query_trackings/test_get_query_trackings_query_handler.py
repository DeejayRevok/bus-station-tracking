from unittest import TestCase
from unittest.mock import Mock

from application.get_query_trackings.get_query_trackings_query import GetQueryTrackingsQuery
from application.get_query_trackings.get_query_trackings_query_handler import GetQueryTrackingsQueryHandler
from domain.passenger.find_passenger_tracking_criteria import FindPassengerTrackingCriteria
from domain.query.query_tracking import QueryTracking
from domain.query.query_tracking_repository import QueryTrackingRepository


class TestGetQueryTrackingsQueryHandler(TestCase):
    def setUp(self) -> None:
        self.query_tracking_repository = Mock(spec=QueryTrackingRepository)
        self.get_query_trackings_query_handler = GetQueryTrackingsQueryHandler(
            query_tracking_repository=self.query_tracking_repository
        )

    def test_handle(self) -> None:
        test_return_query_trackings = [
            QueryTracking(
                id="test_query_id",
                root_passenger_id="test_root_passenger_id",
                name="test_name",
                executor_name="test_executor_name",
                execution_start=None,
                execution_end=None,
                success=True,
                data={},
            ),
        ]
        self.query_tracking_repository.find_by_criteria.return_value = test_return_query_trackings

        response = self.get_query_trackings_query_handler.handle(GetQueryTrackingsQuery())

        self.assertEqual(response.data, test_return_query_trackings)
        self.query_tracking_repository.find_by_criteria.assert_called_once_with(FindPassengerTrackingCriteria())
