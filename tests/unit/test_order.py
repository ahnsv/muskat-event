from app.domain.events import PaymentConfirmed, PaymentPending
from eventsourcing.domain import AggregateCreated
from app.domain.aggregates import Order


def test_order_create_event():
    fake_order = Order(username="FAKE", product_id="FAKE_PRODUCT_ID", sku=1)

    # when

    # then
    events = fake_order.collect_events()
    assert isinstance(events[0], AggregateCreated) is True


def test_order_payment_confirm_event():
    fake_order = Order(username="FAKE", product_id="FAKE_PRODUCT_ID", sku=1)

    fake_order.confirm_payment(38000)

    events = fake_order.collect_events()
    assert isinstance(events[1], PaymentConfirmed)



def test_order_payment_pending_event():
    fake_order = Order(username="FAKE", product_id="FAKE_PRODUCT_ID", sku=1)

    fake_order.confirm_payment(3800)

    events = fake_order.collect_events()
    assert isinstance(events[1], PaymentPending)