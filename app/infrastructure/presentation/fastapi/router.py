from typing import Optional
from uuid import UUID
from app.infrastructure.dependencies.container import Container
from app.domain import commands as cmd
import http
from app.infrastructure.presentation.fastapi.schema import (
    CancelOrderInput,
    CreateOrder,
    OrderOutput,
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
    command = cmd.CreateOrder(**body.dict())
    return usecase.create_new_order(cmd=command)


@router.get("/{order_id}", response_model=OrderOutput)
@inject
def get_order(
    order_id: UUID,
    version: Optional[int] = None,
    usecase: OrderUsecase = Depends(Provide[Container.usecase]),
):
    return usecase.get_order(order_id, version_id=version)


@router.delete("/{order_id}", status_code=http.HTTPStatus.ACCEPTED)
@inject
def cancel_order(
    order_id: UUID,
    body: CancelOrderInput,
    usecase: OrderUsecase = Depends(Provide[Container.usecase]),
):
    command = cmd.CancelOrder(**{"order_id": order_id, **body.dict()})
    usecase.cancel_order(cmd=command)


@router.patch("/{order_id}", status_code=http.HTTPStatus.ACCEPTED)
@inject
def update_order(
    order_id: UUID,
    body: UpdateOrderInput,
    usecase: OrderUsecase = Depends(Provide[Container.usecase]),
):
    command = cmd.UpdateOrder(order_id=order_id, **body.dict())
    usecase.update_order(cmd=command)
