class Scheduler:
    def __init__(self):
        self.events = []

    def add_event(self, event, date, time):
        self.events.append((event, date, time))
