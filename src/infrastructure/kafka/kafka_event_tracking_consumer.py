from datetime import datetime
from typing import Final, Optional

from bus_station.tracking_terminal.models.event_tracking import EventTracking

from application.save_event_tracking.save_event_tracking_command import SaveEventTrackingCommand
from infrastructure.kafka.kafka_passenger_tracking_consumer import KafkaPassengerTrackingConsumer


class KafkaEventTrackingConsumer(KafkaPassengerTrackingConsumer):
    _CONSUMER_GROUP_ID: Final = "EventTrackingConsumer"
    _PASSENGER_TRACKING_CLS: Final = EventTracking

    def _process_passenger_tracking(self, passenger_tracking: EventTracking) -> None:
        save_command = SaveEventTrackingCommand(
            id=passenger_tracking.passenger_id,
            name=passenger_tracking.name,
            executor_name=passenger_tracking.executor_name,
            data=passenger_tracking.data,
            execution_start=self.__datetime_to_str(passenger_tracking.execution_start),
            execution_end=self.__datetime_to_str(passenger_tracking.execution_end),
            success=passenger_tracking.success,
        )
        self._command_bus.transport(save_command)

    def __datetime_to_str(self, datetime_instance: Optional[datetime]) -> Optional[str]:
        if datetime_instance is None:
            return None
        return datetime_instance.isoformat()
