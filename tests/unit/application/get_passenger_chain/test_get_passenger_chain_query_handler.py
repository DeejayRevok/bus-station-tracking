from unittest import TestCase
from unittest.mock import Mock

from application.get_passenger_chain.get_passenger_chain_query import GetPassengerChainQuery
from application.get_passenger_chain.get_passenger_chain_query_handler import GetPassengerChainQueryHandler
from domain.passenger.chain.passenger_chain import PassengerChain
from domain.passenger.chain.passenger_chain_finder import PassengerChainFinder


class TestGetPassengerChainQueryHandler(TestCase):
    def setUp(self) -> None:
        self.passenger_chain_finder = Mock(spec=PassengerChainFinder)
        self.get_passenger_chain_query_handler = GetPassengerChainQueryHandler(
            passenger_chain_finder=self.passenger_chain_finder
        )

    def test_handle(self):
        test_chain = PassengerChain(edges=[])
        self.passenger_chain_finder.find_by_passenger_id.return_value = test_chain

        response = self.get_passenger_chain_query_handler.handle(
            GetPassengerChainQuery(passenger_identifier="test_passenger_id")
        )

        self.assertEqual(response.data, test_chain)
        self.passenger_chain_finder.find_by_passenger_id.assert_called_once_with("test_passenger_id")
