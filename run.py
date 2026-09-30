# import sys

# from importlib import reload
from app import create_app
from config import app_active, app_config

config = app_config[app_active]
config.APP = create_app(app_active)


def main() -> None:
    config.APP.run(host=config.IP_HOST, port=config.PORT_HOST)
    # reload(sys)


if __name__ == "__main__":
    main()
