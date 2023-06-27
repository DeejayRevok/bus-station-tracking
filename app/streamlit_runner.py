from os.path import dirname, join

from streamlit.web.cli import main_run
from yandil.dependency_filler import DependencyFiller

from app.loaders import load_app
from infrastructure.streamlit.services.passenger_chain_service import PassengerChainService
from infrastructure.streamlit.services.trackings_data_service import TrackingsDataService

__STREAMLIT_ENTRY_POINT = join(dirname(dirname(__file__)), "src", "infrastructure", "streamlit", "home.py")


def run() -> None:
    load_app()
    __configure_streamlit_services()
    main_run([__STREAMLIT_ENTRY_POINT])


def __configure_streamlit_services() -> None:
    dependency_filler = DependencyFiller()
    dependency_filler.fill(TrackingsDataService)
    dependency_filler.fill(PassengerChainService)


if __name__ == "__main__":
    run()
