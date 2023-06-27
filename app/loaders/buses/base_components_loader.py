from yandil.container import default_container

from app.loaders.buses.yandil_bus_stop_resolver import YandilBusStopResolver


def load() -> None:
    default_container.add(YandilBusStopResolver)
