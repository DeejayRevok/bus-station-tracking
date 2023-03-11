from app.loaders.buses.query.query_receiver_loader import load as load_query_receiver
from app.loaders.buses.query.sync_query_bus_loader import load as load_sync_query_bus


def load() -> None:
    load_query_receiver()
    load_sync_query_bus()
