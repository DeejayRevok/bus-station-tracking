from dataclasses import dataclass

from bus_station.query_terminal.query import Query


@dataclass(frozen=True)
class GetPassengerChainQuery(Query):
    passenger_identifier: str
