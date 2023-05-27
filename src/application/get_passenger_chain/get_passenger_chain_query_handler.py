from bus_station.query_terminal.query_handler import QueryHandler
from bus_station.query_terminal.query_response import QueryResponse

from application.get_passenger_chain.get_passenger_chain_query import GetPassengerChainQuery
from domain.passenger.chain.passenger_chain_finder import PassengerChainFinder


class GetPassengerChainQueryHandler(QueryHandler):
    def __init__(self, passenger_chain_finder: PassengerChainFinder):
        self.__passenger_chain_finder = passenger_chain_finder

    def handle(self, query: GetPassengerChainQuery) -> QueryResponse:
        return QueryResponse(data=self.__passenger_chain_finder.find_by_passenger_id(query.passenger_identifier))
