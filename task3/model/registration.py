class Registration:
    def __init__(self):
        self.registrations = []

    def register_participant(self, participant, event):
        event.register_participant(participant)
        self.registrations.append((participant, event))
