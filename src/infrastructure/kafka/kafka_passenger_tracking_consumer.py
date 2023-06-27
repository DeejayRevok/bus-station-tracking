from abc import ABC, abstractmethod
from logging import Logger
from typing import Optional

from bus_station.command_terminal.bus.command_bus import CommandBus
from bus_station.tracking_terminal.models.passenger_tracking import PassengerTracking
from confluent_kafka import Message, Producer

from infrastructure.bus_station.passenger_tracking_json_deserializer import PassengerTrackingJSONDeserializer
from infrastructure.kafka.kafka_consumer_creator import KafkaConsumerCreator
from infrastructure.kafka.kafka_topic_creator import KafkaTopicCreator


class KafkaPassengerTrackingConsumer(ABC):
    _CONSUMER_GROUP_ID: Optional[str] = None
    _PASSENGER_TRACKING_CLS: Optional[type] = None

    def __init__(
        self,
        kafka_consumer_creator: KafkaConsumerCreator,
        passenger_tracking_deserializer: PassengerTrackingJSONDeserializer,
        topic_creator: KafkaTopicCreator,
        kafka_producer: Producer,
        command_bus: CommandBus,
        logger: Logger,
    ):
        self.__consumer = kafka_consumer_creator.create(self._CONSUMER_GROUP_ID)
        self.__passenger_tracking_deserializer = passenger_tracking_deserializer
        self.__topic_creator = topic_creator
        self.__producer = kafka_producer
        self.__logger = logger
        self._command_bus = command_bus
        self.__topic_name: Optional[str] = None

    def consume(self):
        self.__setup()
        self.__logger.info(f"Starting consuming from {self.__topic_name}")
        while True:
            try:
                message = self.__consumer.poll(1.0)
            except KeyboardInterrupt:
                break

            if message is None:
                continue
            if message.error():
                self.__logger.error(f"Error consuming from {self.__topic_name}: {message.error()}")
                continue
            self.__process_message(message)

        self.__producer.flush()
        self.__consumer.close()
        self.__logger.info(f"Finished consuming from {self.__topic_name}")

    def __setup(self):
        self.__topic_name = self._PASSENGER_TRACKING_CLS.__name__
        self.__topic_creator.create(self.__topic_name)
        self.__consumer.subscribe([self.__topic_name])

    def __process_message(self, message: Message) -> None:
        message_value = message.value().decode("utf-8")
        self.__logger.info(f"Received message: {message_value}")

        passenger_tracking = self.__passenger_tracking_deserializer.deserialize(message_value)
        try:
            self._process_passenger_tracking(passenger_tracking)
        except Exception as ex:
            self.__logger.warning(f"Error consuming {message_value}. Reason: {ex}")
            if self.__is_retried(message) is False:
                self.__producer.produce(topic=self.__topic_name, value=message_value, headers=[("retried", "")])

    @abstractmethod
    def _process_passenger_tracking(self, passenger_tracking: PassengerTracking) -> None:
        pass

    def __is_retried(self, message: Message) -> bool:
        message_headers = message.headers()
        if message_headers is None:
            return False

        for header_name, header_value in message.headers():
            if header_name == "retried":
                return True
        return False
