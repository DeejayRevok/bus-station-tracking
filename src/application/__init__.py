from application.get_command_trackings import load as load_get_command_trackings
from application.get_event_trackings import load as load_get_event_trackings
from application.get_passenger_chain import load as load_get_passenger_chain
from application.get_query_trackings import load as load_get_query_trackings
from application.save_command_tracking import load as load_save_command_tracking
from application.save_event_tracking import load as load_save_event_tracking
from application.save_passenger_chain_node import load as load_save_passenger_chain_node
from application.save_query_tracking import load as load_save_query_tracking


def load() -> None:
    load_save_command_tracking()
    load_save_event_tracking()
    load_save_query_tracking()
    load_save_passenger_chain_node()
    load_get_command_trackings()
    load_get_event_trackings()
    load_get_query_trackings()
    load_get_passenger_chain()
