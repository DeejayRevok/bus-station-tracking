from pypendency.argument import Argument
from pypendency.builder import container_builder
from pypendency.definition import Definition


def load() -> None:
    container_builder.set_definition(
        Definition(
            "application.save_passenger_chain_node"
            ".save_passenger_chain_node_command_handler.SavePassengerChainNodeCommandHandler",
            "application.save_passenger_chain_node"
            ".save_passenger_chain_node_command_handler.SavePassengerChainNodeCommandHandler",
            [
                Argument.no_kw_argument(
                    "@infrastructure.neo4j.neo4j_passenger_chain_node_repository.Neo4jPassengerChainNodeRepository"
                )
            ],
        )
    )
    container_builder.set_definition(
        Definition(
            "application.save_passenger_chain_node.command_tracking_created_consumer.CommandTrackingCreatedConsumer",
            "application.save_passenger_chain_node.command_tracking_created_consumer.CommandTrackingCreatedConsumer",
            [Argument.no_kw_argument("@bus_station.command_terminal.bus.synchronous.sync_command_bus.SyncCommandBus")],
        )
    )
    container_builder.set_definition(
        Definition(
            "application.save_passenger_chain_node.event_tracking_created_consumer.EventTrackingCreatedConsumer",
            "application.save_passenger_chain_node.event_tracking_created_consumer.EventTrackingCreatedConsumer",
            [Argument.no_kw_argument("@bus_station.command_terminal.bus.synchronous.sync_command_bus.SyncCommandBus")],
        )
    )
