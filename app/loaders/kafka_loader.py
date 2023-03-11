import os

from confluent_kafka.admin import AdminClient
from confluent_kafka.cimpl import Producer
from pypendency.builder import container_builder

from infrastructure.kafka.kafka_consumer_creator import KafkaConsumerCreator


def load() -> None:
    kafka_bootstrap_servers = os.environ.get("BUS_STATION_TRACKING_KAFKA_BOOTSTRAP_SERVERS")
    kafka_consumer_base_config = {"bootstrap.servers": kafka_bootstrap_servers, "auto.offset.reset": "smallest"}
    kafka_consumer_creator = KafkaConsumerCreator(kafka_consumer_base_config)
    container_builder.set("infrastructure.kafka.kafka_consumer_creator.KafkaConsumerCreator", kafka_consumer_creator)

    kafka_admin_client = AdminClient({"bootstrap.servers": kafka_bootstrap_servers})
    container_builder.set("confluent_kafka.admin.AdminClient", kafka_admin_client)

    kafka_producer = Producer(
        {
            "bootstrap.servers": kafka_bootstrap_servers,
            "client.id": "bus-station-tracking-retrier",
            "queue.buffering.max.ms": 10,
        }
    )
    container_builder.set("confluent_kafka.cimpl.Producer", kafka_producer)
