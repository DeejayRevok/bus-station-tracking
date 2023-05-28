from tempfile import NamedTemporaryFile
from typing import Optional

from networkx import DiGraph
from pyvis.network import Network
from streamlit import components, markdown

from domain.passenger.chain.passenger_chain import PassengerChain
from domain.passenger.chain.passenger_chain_node import PassengerChainNode
from domain.passenger.chain.passenger_chain_node_type import PassengerChainNodeType
from infrastructure.streamlit.components.passenger_chain_filter import PassengerChainFilter


class PassengerChainView:
    __NODE_LABEL_PATTERN = "{name}\n{id}"
    __PASSENGER_CHAIN_NODE_TYPE_ATTRS = {
        PassengerChainNodeType.COMMAND: {"color": "lightblue"},
        PassengerChainNodeType.EVENT: {"color": "green"},
    }
    __FILTERED_PASSENGER_NODE_ATTRS = {"color": "black"}

    def __init__(self, passenger_chain: Optional[PassengerChain], passenger_chain_filter: PassengerChainFilter):
        self.__passenger_chain = passenger_chain
        self.__passenger_chain_filter = passenger_chain_filter

    def build(self) -> None:
        if self.__passenger_chain is None:
            if self.__passenger_chain_filter.passenger_id is not None:
                markdown(f"Chain for passenger {self.__passenger_chain_filter.passenger_id} not found")
            return

        network_html = self.__get_network_html(self.__transform_graph_to_network(self.__build_graph()))
        components.v1.html(network_html, height=600)

    def __build_graph(self) -> DiGraph:
        chain_graph = DiGraph()
        for start_node, end_node in self.__passenger_chain.edges:
            if self.__passenger_chain_filter.passenger_id == start_node.id:
                self.__build_filtered_passenger_node(chain_graph, start_node)
            else:
                self.__build_node(chain_graph, start_node)

            if self.__passenger_chain_filter.passenger_id == end_node.id:
                self.__build_filtered_passenger_node(chain_graph, end_node)
            else:
                self.__build_node(chain_graph, end_node)

            self.__build_edge(chain_graph, start_node, end_node)

        return chain_graph

    def __build_filtered_passenger_node(self, chain_graph: DiGraph, node: PassengerChainNode) -> None:
        chain_graph.add_node(
            node_for_adding=node.id, label=node.name, color=self.__FILTERED_PASSENGER_NODE_ATTRS["color"], title=node.id
        )

    def __build_node(self, chain_graph: DiGraph, node: PassengerChainNode) -> None:
        node_type_attrs = self.__PASSENGER_CHAIN_NODE_TYPE_ATTRS[node.type]
        chain_graph.add_node(node_for_adding=node.id, label=node.name, color=node_type_attrs["color"], title=node.id)

    def __build_edge(self, chain_graph: DiGraph, start_node: PassengerChainNode, end_node: PassengerChainNode) -> None:
        chain_graph.add_edge(start_node.id, end_node.id)

    def __transform_graph_to_network(self, chain_graph: DiGraph) -> Network:
        chain_graph_network = Network()
        chain_graph_network.from_nx(chain_graph)
        return chain_graph_network

    def __get_network_html(self, chain_graph_network: Network) -> str | bytes:
        with NamedTemporaryFile(suffix=".html") as temp_file:
            chain_graph_network.show(temp_file.name, notebook=False)
            temp_file.seek(0)
            return temp_file.read()
