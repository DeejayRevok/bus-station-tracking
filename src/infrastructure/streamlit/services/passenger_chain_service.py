from typing import Optional

from bus_station.query_terminal.bus.synchronous.sync_query_bus import SyncQueryBus

from application.get_passenger_chain.get_passenger_chain_query import GetPassengerChainQuery
from domain.passenger.chain.passenger_chain import PassengerChain
from infrastructure.streamlit.components.passenger_chain_filter import PassengerChainFilter


class PassengerChainService:
    def __init__(self, passenger_chain_filter: PassengerChainFilter, query_bus: Optional[SyncQueryBus] = None):
        self.__query_bus = query_bus
        self.__passenger_chain_filter = passenger_chain_filter

    def get_passenger_chain(self) -> Optional[PassengerChain]:
        passenger_id = self.__passenger_chain_filter.passenger_id
        if passenger_id is None:
            return None

        get_passenger_chain_query = GetPassengerChainQuery(passenger_identifier=passenger_id)
        return self.__query_bus.transport(get_passenger_chain_query).data
