from typing import Optional
from uuid import UUID
from app.application.exceptions import DomainNotFound
from eventsourcing.domain import AggregateEvent
from app.domain.aggregates import Order
from eventsourcing.application import Application, AggregateNotFound


# TODO(humphrey): DIP를 적용한다
class OrderUsecase(Application):
    def _get_order(self, order_id) -> Order:
        try:
            found_order: Order = self.repository.get(order_id)
            return found_order
        except AggregateNotFound:
            raise DomainNotFound()

    def create_new_order(
        self, username: str, sku: int, product_id: str = "muskat"
    ) -> UUID:
        new_order = Order(username=username, product_id=product_id, sku=sku)
        self.save(new_order)
        return new_order.id

    def handle_payment(self, amount: int, order_id: str) -> AggregateEvent:
        found_order = self._get_order(order_id=order_id)
        found_order.confirm_payment(amount=amount)
        return found_order.history[-1]

    def cancel_order(self, order_id, reason) -> AggregateEvent:
        found_order = self._get_order(order_id=order_id)
        found_order.cancel(reason=reason)
        assert found_order.is_active is False
        return found_order.history[-1]

    def update_order(self, order_id: str, sku: int, username: Optional[str] = None):
        found_order = self._get_order(order_id=order_id)
        found_order.update(sku, username)
        assert found_order.sku == sku
        assert found_order.username == username
        return found_order.history[-1]
