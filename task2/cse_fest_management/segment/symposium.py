from interfaces.segment_interface import SegmentInterface
from models.event import Event

class SymposiumTalk(Event, SegmentInterface):
    def __init__(self, name, description):
        super().__init__(name, description)

    def register_participant(self, participant):
        # Register a participant specific to SymposiumTalk
        self.participants.append(participant)

    def start_event(self):
        # Start the Symposium Talk event
        print("Symposium Talk is now starting!")
