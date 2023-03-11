from os.path import dirname, join

from streamlit.web.cli import main_run

from app.loaders import load_app

__STREAMLIT_ENTRY_POINT = join(dirname(dirname(__file__)), "src", "infrastructure", "streamlit", "home.py")


def run() -> None:
    load_app()
    main_run([__STREAMLIT_ENTRY_POINT])


if __name__ == "__main__":
    run()
