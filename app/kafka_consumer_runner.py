from argparse import ArgumentParser
from typing import Type

from yandil.container import default_container

from app.loaders import load_app
from domain.passenger.passenger_tracking_consumer import PassengerTrackingConsumer
from infrastructure.kafka.kafka_command_tracking_consumer import KafkaCommandTrackingConsumer
from infrastructure.kafka.kafka_event_tracking_consumer import KafkaEventTrackingConsumer
from infrastructure.kafka.kafka_query_tracking_consumer import KafkaQueryTrackingConsumer


def run() -> None:
    load_app()
    args = __load_args()
    consumer: PassengerTrackingConsumer = default_container[
        __get_passenger_tracking_consumer_class(args["passenger_tracking"])
    ]
    consumer.consume()


def __load_args() -> dict:
    arg_solver = ArgumentParser(description="Event consumer runner")
    arg_solver.add_argument(
        "-pt",
        "--passenger_tracking",
        required=True,
        help="Passenger tracking to consume",
        choices=("command_tracking", "event_tracking", "query_tracking"),
    )

    return vars(arg_solver.parse_args())


def __get_passenger_tracking_consumer_class(passenger_tracking_type: str) -> Type:
    if passenger_tracking_type == "command_tracking":
        return KafkaCommandTrackingConsumer
    if passenger_tracking_type == "event_tracking":
        return KafkaEventTrackingConsumer
    if passenger_tracking_type == "query_tracking":
        return KafkaQueryTrackingConsumer
    raise NotImplementedError(f"Runner for {passenger_tracking_type} not implemented")


if __name__ == "__main__":
    run()
