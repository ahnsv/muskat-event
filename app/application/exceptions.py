from enum import Enum


class ErrorMessage(str, Enum):
    DOMAIN_NOT_FOUND = "도메인 모델을 찾을 수 없습니다"


class ApplicationException(Exception):
    def __init__(self, message: str, code: int = 101) -> None:
        self.message = message
        self.code = code


class DomainNotFound(ApplicationException):
    def __init__(self, message: str = ErrorMessage.DOMAIN_NOT_FOUND) -> None:
        super().__init__(message=message)
