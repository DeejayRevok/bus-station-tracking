from app.loaders.buses import load as load_buses
from app.loaders.buses.command.handlers_registry import register as register_command_handlers
from app.loaders.buses.command.middlewares_loader import load as load_command_bus_middlewares
from app.loaders.buses.event.consumers_registry import register as register_event_consumers
from app.loaders.buses.event.middlewares_loader import load as load_event_bus_middlewares
from app.loaders.buses.query.handlers_registry import register as register_query_handlers
from app.loaders.buses.query.middlewares_loader import load as load_query_bus_middlewares
from app.loaders.container_loader import load as load_container
from app.loaders.database_loader import load as load_database
from app.loaders.kafka_loader import load as load_kafka
from app.loaders.logger_loader import load as load_logger
from app.loaders.neo4j_loader import load as load_neo4j


def load_app():
    load_logger()
    load_kafka()
    load_neo4j()
    load_container()
    load_buses()
    load_database()

    load_command_bus_middlewares()
    load_query_bus_middlewares()
    load_event_bus_middlewares()
    register_command_handlers()
    register_query_handlers()
    register_event_consumers()
