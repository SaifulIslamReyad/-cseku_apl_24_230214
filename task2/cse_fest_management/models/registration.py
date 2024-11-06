class Registration:
    def __init__(self):
        self.registrations = []

    def register(self, participant, event):
        event.add_participant(participant)
        self.registrations.append((participant, event))