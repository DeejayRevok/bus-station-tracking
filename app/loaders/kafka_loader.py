import os

from confluent_kafka.admin import AdminClient
from confluent_kafka.cimpl import Producer
from yandil.container import default_container

from infrastructure.kafka.kafka_consumer_creator import KafkaConsumerCreator


def load() -> None:
    kafka_bootstrap_servers = os.environ.get("BUS_STATION_TRACKING_KAFKA_BOOTSTRAP_SERVERS")
    kafka_consumer_base_config = {"bootstrap.servers": kafka_bootstrap_servers, "auto.offset.reset": "smallest"}
    kafka_consumer_creator = KafkaConsumerCreator(kafka_consumer_base_config)
    default_container[KafkaConsumerCreator] = kafka_consumer_creator

    kafka_admin_client = AdminClient({"bootstrap.servers": kafka_bootstrap_servers})
    default_container[AdminClient] = kafka_admin_client

    kafka_producer = Producer(
        {
            "bootstrap.servers": kafka_bootstrap_servers,
            "client.id": "bus-station-tracking-retrier",
            "queue.buffering.max.ms": 10,
        }
    )
    default_container[Producer] = kafka_producer
