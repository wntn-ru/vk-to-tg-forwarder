from pydantic import BaseSettings

class Settings(BaseSettings):
    VK_TOKEN: str
    VK_PEER_ID: int
    TG_TOKEN: str
    TG_CHAT_ID: int

    class Config:
        env_file = '.env'

settings = Settings()