from interfaces.segment_interface import SegmentInterface
from models.event import Event

class CompetitiveProgramming(Event, SegmentInterface):
    def __init__(self, name, description):
        super().__init__(name, description)

    def register_participant(self, participant):
        # Register a participant for Competitive Programming
        self.participants.append(participant)

    def start_event(self):
        # Start the Competitive Programming event
        print("Competitive Programming Contest is now starting!")
