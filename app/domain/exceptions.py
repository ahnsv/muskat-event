from enum import Enum


class DomainException(Exception):
    def __init__(self, message: str, code: int = 100) -> None:
        self.message = message
        self.code = code


class InsufficientPaymentException(DomainException):
    name = "insufficient_payment"


class ErrorMessage(str, Enum):
    INSUFFICIENT_PAYMENT = "주문 금액보다 부족합니다"
