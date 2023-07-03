from bus_station.bus_stop.resolvers.yandil_bus_stop_resolver import YandilBusStopResolver
from yandil.container import default_container


def load() -> None:
    default_container.add(YandilBusStopResolver)
