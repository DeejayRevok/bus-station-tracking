from datetime import datetime
from typing import Final, Optional

from bus_station.tracking_terminal.models.query_tracking import QueryTracking

from application.save_query_tracking.save_query_tracking_command import SaveQueryTrackingCommand
from infrastructure.kafka.kafka_passenger_tracking_consumer import KafkaPassengerTrackingConsumer


class KafkaQueryTrackingConsumer(KafkaPassengerTrackingConsumer):
    _CONSUMER_GROUP_ID: Final = "QueryTrackingConsumer"
    _PASSENGER_TRACKING_CLS: Final = QueryTracking

    def _process_passenger_tracking(self, passenger_tracking: QueryTracking) -> None:
        save_command = SaveQueryTrackingCommand(
            id=passenger_tracking.passenger_id,
            name=passenger_tracking.name,
            executor_name=passenger_tracking.executor_name,
            data=passenger_tracking.data,
            execution_start=self.__datetime_to_str(passenger_tracking.execution_start),
            execution_end=self.__datetime_to_str(passenger_tracking.execution_end),
            success=passenger_tracking.success,
            response_data=passenger_tracking.response_data,
        )
        self._command_bus.transport(save_command)

    def __datetime_to_str(self, datetime_instance: Optional[datetime]) -> Optional[str]:
        if datetime_instance is None:
            return None
        return datetime_instance.isoformat()
