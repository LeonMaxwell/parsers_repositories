from pydantic import BaseConfig
from utils.db import DatabaseParser


class AppConfig(BaseConfig):
    service_name: str = "Parsers Git Repositories"
    name: str = "parsers-git-repositories"
    host: str = "0.0.0.0"
    port: int = 7000
    docs_enable: bool = True
    url_prefix: str = "/api"
    db = DatabaseParser()


app = AppConfig()