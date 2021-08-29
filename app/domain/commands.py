from uuid import UUID
from pydantic import BaseModel, Field


class BaseCommand(BaseModel):
    pass


class CreateOrder(BaseCommand):
    username: str
    sku: int
    product_id: str = Field(default="muskat")


class HandlePayment(BaseCommand):
    amount: int
    order_id: UUID


class CancelOrder(BaseCommand):
    order_id: UUID
    reason: str

class UpdateOrder(BaseCommand):
    order_id: UUID
    sku: int
    username: str

