from os import environ

from neomodel import config

__CONNECTION_URL_PATTERN = "bolt://{username}:{password}@{host}:{port}"


def load() -> None:
    config.DATABASE_URL = __CONNECTION_URL_PATTERN.format(
        username=environ["BUS_STATION_TRACKING_NEO4J_USERNAME"],
        password=environ["BUS_STATION_TRACKING_NEO4J_PASSWORD"],
        host=environ["BUS_STATION_TRACKING_NEO4J_HOST"],
        port=environ["BUS_STATION_TRACKING_NEO4J_PORT"],
    )
