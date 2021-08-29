from app.application.usecase import OrderUsecase
from dependency_injector import containers, providers
from pydantic import BaseSettings, Field
from eventsourcing.cipher import AESCipher


class Config(BaseSettings):
    cipher_key: str = Field(
        default=AESCipher.create_key(num_bytes=32),
    )
    cipher_topic: str = Field(
        default="eventsourcing.cipher:AESCipher", env="cipher_topic"
    )
    compressor_topic: str = Field(
        default="eventsourcing.compressor:ZlibCompressor", env="compressor_topic"
    )

    def set_env_vars(self):
        import os

        os.environ["CIPHER_KEY"] = self.cipher_key
        os.environ["CIPHER_TOPIC"] = self.cipher_topic
        os.environ["COMPRESSOR_TOPIC"] = self.compressor_topic


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    usecase = providers.Factory(
        OrderUsecase,
    )
