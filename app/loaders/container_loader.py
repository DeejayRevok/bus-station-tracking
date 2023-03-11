from application import load as load_application
from infrastructure import load as load_infrastructure


def load():
    load_infrastructure()
    load_application()
