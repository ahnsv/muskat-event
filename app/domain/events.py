from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional
from eventsourcing.domain import AggregateEvent, TAggregate
from enum import Enum


class PaymentConfirmed(AggregateEvent):
    payed_at: datetime = field(default_factory=datetime.now)

    def apply(self, aggregate) -> None:
        aggregate.history += (self,)


class PaymentReceived(AggregateEvent):
    amount: int


class PaymentPending(AggregateEvent):
    reason: str

    def apply(self, aggregate) -> None:
        aggregate.history += (self,)


class CancelReason(str, Enum):
    CHANGE_OF_MIND = "단순 변심"


class OrderCanceled(AggregateEvent):
    reason: CancelReason

    def apply(self, aggregate) -> None:
        aggregate.history += (self,)
        aggregate.is_active = False


class OrderUpdated(AggregateEvent):
    sku: int
    username: Optional[str] = None

    def apply(self, aggregate: TAggregate) -> None:
        aggregate.sku = self.sku
        if self.username:
            aggregate.username = self.username
        aggregate.history += (self,)
