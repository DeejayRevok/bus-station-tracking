from os.path import dirname, join

from yandil.loaders.self_discover_dependency_loader import SelfDiscoverDependencyLoader

sources_path = join(dirname(dirname(dirname(__file__))), "src")


def load():
    SelfDiscoverDependencyLoader(
        excluded_modules={"streamlit"},
        discovery_base_path=sources_path,
        sources_root_path=sources_path,
    ).load()
