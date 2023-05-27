from bus_station.bus_stop.resolvers.pypendency_bus_stop_resolver import PypendencyBusStopResolver
from pypendency.builder import container_builder


def load() -> None:
    container_builder.set(
        "bus_station.bus_stop.resolvers.pypendency_bus_stop_resolver.PypendencyBusStopResolver",
        PypendencyBusStopResolver(container_builder),
    )
