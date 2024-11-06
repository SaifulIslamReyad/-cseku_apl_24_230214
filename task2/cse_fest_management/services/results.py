class Results:
    def __init__(self):
        self.results = {}

    def add_result(self, event, participant, score):
        if event not in self.results:
            self.results[event] = []
        self.results[event].append((participant, score))

    def display_results(self, event):
        print(f"Results for {event.name}:")
        for participant, score in self.results.get(event, []):
            print(f"{participant.name}: {score}")