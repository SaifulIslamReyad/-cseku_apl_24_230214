class Scheduler:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)
        print(f"{event.name} has been scheduled.")