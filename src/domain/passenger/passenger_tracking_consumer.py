from typing import Protocol


class PassengerTrackingConsumer(Protocol):
    def consume(self) -> None:
        ...
