from pypendency.builder import container_builder
from pypendency.definition import Definition


def load() -> None:
    container_builder.set_definition(
        Definition(
            "infrastructure.bus_station.command_tracking_json_deserializer.CommandTrackingJSONDeserializer",
            "infrastructure.bus_station.command_tracking_json_deserializer.CommandTrackingJSONDeserializer",
        )
    )
    container_builder.set_definition(
        Definition(
            "infrastructure.bus_station.event_tracking_json_deserializer.EventTrackingJSONDeserializer",
            "infrastructure.bus_station.event_tracking_json_deserializer.EventTrackingJSONDeserializer",
        )
    )
    container_builder.set_definition(
        Definition(
            "infrastructure.bus_station.query_tracking_json_deserializer.QueryTrackingJSONDeserializer",
            "infrastructure.bus_station.query_tracking_json_deserializer.QueryTrackingJSONDeserializer",
        )
    )
