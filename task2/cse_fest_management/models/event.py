class Event:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.participants = []

    def add_participant(self, participant):
        self.participants.append(participant)