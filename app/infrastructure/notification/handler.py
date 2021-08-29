from abc import ABC, abstractmethod


class NotificationHandler(ABC):
    @abstractmethod
    def handle(self):
        pass
