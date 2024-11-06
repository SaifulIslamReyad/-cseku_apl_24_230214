from interfaces.segment_interface import SegmentInterface
from models.event import Event

class Datathon(Event, SegmentInterface):
    def __init__(self, name, description):
        super().__init__(name, description)

    def register_participant(self, participant):
        # Register a participant for Datathon
        self.participants.append(participant)

    def start_event(self):
        # Start the Datathon event
        print("Datathon is now live!")
