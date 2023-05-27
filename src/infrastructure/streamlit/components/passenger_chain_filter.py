from typing import Optional

from streamlit import text_input


class PassengerChainFilter:
    def __init__(self):
        self.__passenger_id: Optional[str] = None

    @property
    def passenger_id(self) -> Optional[str]:
        if self.__passenger_id == "":
            return None
        return self.__passenger_id

    def build(self) -> None:
        self.__passenger_id = text_input("Passenger identifier")
