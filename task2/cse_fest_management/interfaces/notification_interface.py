from abc import ABC, abstractmethod

class NotificationInterface(ABC):
    @abstractmethod
    def notify_participant(self, participant, message):
        pass