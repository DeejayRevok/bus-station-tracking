from os.path import dirname, join
from pathlib import Path

from yandil.loaders.self_discover_dependency_loader import SelfDiscoverDependencyLoader

sources_path = join(dirname(dirname(dirname(__file__))), "src")


def load():
    kafka_module_path = Path(join(sources_path, "infrastructure", "kafka"))
    bus_station_module_path = Path(join(sources_path, "infrastructure", "bus_station"))
    SelfDiscoverDependencyLoader(
        excluded_modules={"streamlit"},
        discovery_base_path=sources_path,
        sources_root_path=sources_path,
        mandatory_modules={kafka_module_path, bus_station_module_path},
    ).load()
