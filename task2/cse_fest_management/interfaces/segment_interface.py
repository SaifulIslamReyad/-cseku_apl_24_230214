from abc import ABC, abstractmethod

class SegmentInterface(ABC):
    @abstractmethod
    def register_participant(self, participant):
        pass

    @abstractmethod
    def start_event(self):
        pass