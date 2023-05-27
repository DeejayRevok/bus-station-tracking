from infrastructure.bus_station import load as load_bus_station
from infrastructure.kafka import load as load_kafka
from infrastructure.neo4j import load as load_neo4j
from infrastructure.sqlalchemy import load as load_sqlalchemy


def load() -> None:
    load_sqlalchemy()
    load_bus_station()
    load_kafka()
    load_neo4j()
