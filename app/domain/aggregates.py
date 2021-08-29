from app.domain.exceptions import ErrorMessage, InsufficientPaymentException
from app.domain.events import PaymentConfirmed, PaymentPending, PaymentReceived
from dataclasses import dataclass, field
from typing import List
from eventsourcing.domain import Aggregate, AggregateEvent, event

BASE_PRICE = 38000


@dataclass
class Order(Aggregate):
    username: str
    product_id: str
    sku: int
    history: List[AggregateEvent] = field(default_factory=list, init=False)

    def _check_payment_amount(self, paid_amount: int):
        condition = paid_amount == self.price
        err = (
            InsufficientPaymentException(message=ErrorMessage.INSUFFICIENT_PAYMENT)
            if condition is False
            else None
        )
        return condition, err

    @property
    def price(self):
        return self.sku * BASE_PRICE

    @event(PaymentReceived)
    def confirm_payment(self, amount):
        _, err = self._check_payment_amount(amount)
        if err:
            if isinstance(err, InsufficientPaymentException):
                self.trigger_event(PaymentPending, reason=err.name)
            return

        self.trigger_event(PaymentConfirmed)
