from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_host: str = "localhost"
    db_port: int = 3306
    db_user: str
    db_password: str
    db_name: str = "opencalendar"
    uvi_host: str = "127.0.0.1"
    uvi_port: int = 8000