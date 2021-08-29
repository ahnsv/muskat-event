from typing import List
from app.domain.events import CancelReason
from pydantic import BaseModel, Field


class CreateOrder(BaseModel):
    username: str
    sku: int


class CancelOrderInput(BaseModel):
    reason: CancelReason


class UpdateOrderInput(BaseModel):
    sku: int
    username: str


class OrderOutput(BaseModel):
    username: str
    product_id: str
    sku: int
    history: List = Field(default_factory=list, init=False)
    is_active: bool = Field(default=True)
