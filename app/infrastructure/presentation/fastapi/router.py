from app.infrastructure.dependencies.container import Container
import http
from app.infrastructure.presentation.fastapi.schema import (
    CancelOrderInput,
    CreateOrder,
    UpdateOrderInput,
)
from dependency_injector.wiring import inject, Provide
from fastapi.params import Depends
from app.application.usecase import OrderUsecase
from fastapi import APIRouter

router = APIRouter(prefix="/orders")


@router.post("/", status_code=http.HTTPStatus.CREATED)
@inject
def create_order(
    body: CreateOrder, usecase: OrderUsecase = Depends(Provide[Container.usecase])
):
    new_order_id = usecase.create_new_order(username=body.username, sku=body.sku)
    return new_order_id


@router.get("/{order_id}")
@inject
def get_order(
    order_id: str, usecase: OrderUsecase = Depends(Provide[Container.usecase])
):
    return usecase._get_order(order_id)


@router.delete("/{order_id}", status_code=http.HTTPStatus.ACCEPTED)
@inject
def cancel_order(
    order_id: str,
    body: CancelOrderInput,
    usecase: OrderUsecase = Depends(Provide[Container.usecase]),
):
    usecase.cancel_order(order_id, reason=body.reason)


@router.patch("/{order_id}", status_code=http.HTTPStatus.ACCEPTED)
@inject
def update_order(
    order_id: str,
    body: UpdateOrderInput,
    usecase: OrderUsecase = Depends(Provide[Container.usecase]),
):
    usecase.update_order(order_id, sku=body.sku, username=body.username)
