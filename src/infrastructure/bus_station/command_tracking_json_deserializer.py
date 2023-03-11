from bus_station.tracking_terminal.models.command_tracking import CommandTracking

from infrastructure.bus_station.passenger_tracking_json_deserializer import PassengerTrackingJSONDeserializer


class CommandTrackingJSONDeserializer(PassengerTrackingJSONDeserializer[CommandTracking]):
    _PASSENGER_TARGET_CLASS = CommandTracking