from app.domain.events import (
    CancelReason,
    OrderCanceled,
    OrderUpdated,
    PaymentConfirmed,
    PaymentPending,
)
from app.application.usecase import OrderUsecase


def create_test_usecase():
    usecase = OrderUsecase()
    new_order_id = usecase.create_new_order(username="FAKE", sku=1)
    return usecase, new_order_id


def test_usecase_create_new_order():
    _, fake_new_order_id = create_test_usecase()

    assert fake_new_order_id is not None


def test_usecase_confirm_order():
    usecase, fake_new_order_id = create_test_usecase()

    result = usecase.handle_payment(amount=38000, order_id=fake_new_order_id)

    assert isinstance(result, PaymentConfirmed) is True


def test_usecase_confirm_order_with_pending_state():
    usecase, fake_new_order_id = create_test_usecase()

    result = usecase.handle_payment(amount=3800, order_id=fake_new_order_id)

    assert isinstance(result, PaymentPending) is True


def test_usecase_cancel_order():
    usecase, fake_new_order_id = create_test_usecase()
    result = usecase.cancel_order(
        order_id=fake_new_order_id, reason=CancelReason.CHANGE_OF_MIND
    )
    assert isinstance(result, OrderCanceled)


def test_usecase_update_order():
    usecase, fake_new_order_id = create_test_usecase()

    result = usecase.update_order(
        order_id=fake_new_order_id, sku=2, username="updated_user"
    )
    assert isinstance(result, OrderUpdated)
