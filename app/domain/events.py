from dataclasses import dataclass, field
from datetime import datetime
from eventsourcing.domain import AggregateEvent


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
