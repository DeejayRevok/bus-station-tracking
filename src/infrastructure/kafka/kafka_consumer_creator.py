from confluent_kafka import Consumer


class KafkaConsumerCreator:
    def __init__(self, kafka_consumer_base_config: dict):
        self.__kafka_consumer_base_config = kafka_consumer_base_config

    def create(self, group_id: str) -> Consumer:
        consumer_config = self.__kafka_consumer_base_config
        consumer_config["group.id"] = group_id
        return Consumer(consumer_config)
