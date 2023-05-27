from datetime import datetime
from typing import Final, Optional

from bus_station.tracking_terminal.models.command_tracking import CommandTracking

from application.save_command_tracking.save_command_tracking_command import SaveCommandTrackingCommand
from infrastructure.kafka.kafka_passenger_tracking_consumer import KafkaPassengerTrackingConsumer


class KafkaCommandTrackingConsumer(KafkaPassengerTrackingConsumer):
    _CONSUMER_GROUP_ID: Final = "CommandTrackingConsumer"
    _PASSENGER_TRACKING_CLS: Final = CommandTracking

    def _process_passenger_tracking(self, passenger_tracking: CommandTracking) -> None:
        save_command = SaveCommandTrackingCommand(
            id=passenger_tracking.passenger_id,
            passenger_root_id=passenger_tracking.root_passenger_id,
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
