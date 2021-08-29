from app.domain.events import CancelReason
from pydantic import BaseModel


class CreateOrder(BaseModel):
    username: str
    sku: int


class CancelOrderInput(BaseModel):
    reason: CancelReason


class UpdateOrderInput(BaseModel):
    sku: int
    username: str
