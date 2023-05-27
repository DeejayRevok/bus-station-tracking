from streamlit import set_page_config, title

from infrastructure.streamlit.components.passenger_chain_filter import PassengerChainFilter
from infrastructure.streamlit.components.passenger_chain_view import PassengerChainView
from infrastructure.streamlit.services.passenger_chain_service import PassengerChainService

set_page_config(page_title="Bus station tracking", layout="wide")
title("Passenger chains")

passenger_chain_filter = PassengerChainFilter()
passenger_chain_filter.build()

passenger_chain_service = PassengerChainService(passenger_chain_filter)
passenger_chain = passenger_chain_service.get_passenger_chain()

PassengerChainView(passenger_chain, passenger_chain_filter).build()
