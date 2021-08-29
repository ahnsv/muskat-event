from app.domain import commands
from typing import Optional
from uuid import UUID
from app.application.exceptions import DomainNotFound
from eventsourcing.domain import AggregateEvent
from app.domain.aggregates import Order
from eventsourcing.application import Application, AggregateNotFound


# TODO(humphrey): DIP를 적용한다
class OrderUsecase(Application):
    def _get_order(self, order_id: UUID, version_id: int = None) -> Order:
        try:
            found_order: Order = self.repository.get(order_id)
            return found_order
        except AggregateNotFound as err:
            raise DomainNotFound()

    def create_new_order(self, cmd: commands.CreateOrder) -> UUID:
        new_order = Order.create(
            username=cmd.username, product_id=cmd.product_id, sku=cmd.sku
        )
        self.save(new_order)  # NOTE(humphrey): save가 안되는 거 같음...
        return new_order.id

    def handle_payment(self, cmd: commands.HandlePayment) -> AggregateEvent:
        found_order = self._get_order(order_id=cmd.order_id)
        found_order.confirm_payment(amount=cmd.amount)
        return found_order.history[-1]

    def cancel_order(self, cmd: commands.CancelOrder) -> AggregateEvent:
        found_order = self._get_order(order_id=cmd.order_id)
        found_order.cancel(reason=cmd.reason)
        assert found_order.is_active is False
        self.save(found_order)
        return found_order.history[-1]

    def update_order(self, cmd: commands.UpdateOrder):
        found_order = self._get_order(order_id=cmd.order_id)
        found_order.update(cmd.sku, cmd.username)
        assert found_order.sku == cmd.sku
        assert found_order.username == cmd.username
        self.save(found_order)
        return found_order.history[-1]
