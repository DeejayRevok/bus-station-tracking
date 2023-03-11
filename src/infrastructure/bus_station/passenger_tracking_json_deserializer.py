from datetime import datetime
from json import loads
from typing import Generic, Optional, TypeVar

from bus_station.tracking_terminal.models.passenger_tracking import PassengerTracking

P = TypeVar("P", bound=PassengerTracking)


class PassengerTrackingJSONDeserializer(Generic[P]):
    _PASSENGER_TARGET_CLASS = PassengerTracking

    def deserialize(self, passenger_tracking_serialized: str) -> P:
        passenger_tracking_data: dict = loads(passenger_tracking_serialized)
        for tracking_data_key, tracking_data_value in passenger_tracking_data.items():
            if tracking_data_key in ("execution_start", "execution_end"):
                passenger_tracking_data[tracking_data_key] = self.__transform_str_to_datetime(tracking_data_value)

        return self._PASSENGER_TARGET_CLASS(**passenger_tracking_data)

    def __transform_str_to_datetime(self, datetime_str: Optional[str]) -> Optional[datetime]:
        if datetime_str is None:
            return None
        return datetime.fromisoformat(datetime_str)
