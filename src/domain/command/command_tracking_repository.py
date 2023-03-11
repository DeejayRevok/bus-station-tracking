from abc import ABC

from domain.command.command_tracking import CommandTracking
from domain.passenger.passenger_tracking_repository import PassengerTrackingRepository


class CommandTrackingRepository(PassengerTrackingRepository[CommandTracking], ABC):
    pass
