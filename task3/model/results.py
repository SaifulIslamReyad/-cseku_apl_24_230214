class Results:
    def __init__(self):
        self.results = {}

    def add_result(self, event, participant, score):
        if event not in self.results:
            self.results[event] = []
        self.results[event].append((participant, score))
