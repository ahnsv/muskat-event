from abc import ABC, abstractmethod


class NotificationListener(ABC):
    @abstractmethod
    def listen(self, event: ...) -> ...:
        ...
