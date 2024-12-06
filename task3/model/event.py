class Event:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.participants = []

    def register_participant(self, participant):
        self.participants.append(participant)

    def start_event(self):
        return f"{self.name} is now starting!"
