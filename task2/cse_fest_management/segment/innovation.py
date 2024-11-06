from interfaces.segment_interface import SegmentInterface
from models.event import Event

class InnovationShowcase(Event, SegmentInterface):
    def __init__(self, name, description):
        super().__init__(name, description)

    def register_participant(self, participant):
        # Register a participant for Innovation Showcase
        self.participants.append(participant)

    def start_event(self):
        # Start the Innovation Showcase event
        print("Innovation Showcase is now starting!")
