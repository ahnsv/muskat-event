from app.application.usecase import OrderUsecase
from dependency_injector import containers, providers

class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    usecase = providers.Factory(OrderUsecase, )