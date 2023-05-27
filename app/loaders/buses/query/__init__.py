from app.loaders.buses.query.sync_query_bus_loader import load as load_sync_query_bus


def load() -> None:
    load_sync_query_bus()
