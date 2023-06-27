from datetime import datetime
from logging import Logger
from typing import Final, Optional

from bus_station.command_terminal.bus.command_bus import CommandBus
from bus_station.tracking_terminal.models.event_tracking import EventTracking
from confluent_kafka import Producer

from application.save_event_tracking.save_event_tracking_command import SaveEventTrackingCommand
from infrastructure.bus_station.event_tracking_json_deserializer import EventTrackingJSONDeserializer
from infrastructure.kafka.kafka_consumer_creator import KafkaConsumerCreator
from infrastructure.kafka.kafka_passenger_tracking_consumer import KafkaPassengerTrackingConsumer
from infrastructure.kafka.kafka_topic_creator import KafkaTopicCreator


class KafkaEventTrackingConsumer(KafkaPassengerTrackingConsumer):
    _CONSUMER_GROUP_ID: Final = "EventTrackingConsumer"
    _PASSENGER_TRACKING_CLS: Final = EventTracking

    def __init__(
        self,
        kafka_consumer_creator: KafkaConsumerCreator,
        passenger_tracking_deserializer: EventTrackingJSONDeserializer,
        topic_creator: KafkaTopicCreator,
        kafka_producer: Producer,
        command_bus: CommandBus,
        logger: Logger,
    ):
        super().__init__(
            kafka_consumer_creator,
            passenger_tracking_deserializer,
            topic_creator,
            kafka_producer,
            command_bus,
            logger,
        )

    def _process_passenger_tracking(self, passenger_tracking: EventTracking) -> None:
        save_command = SaveEventTrackingCommand(
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
