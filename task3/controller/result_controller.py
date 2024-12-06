class ResultController:
    def __init__(self, result_model, result_view):
        self.result_model = result_model
        self.result_view = result_view

    def add_result(self, event, participant, score):
        self.result_model.add_result(event, participant, score)

    def display_results(self, event):
        results = self.result_model.results.get(event, [])
        return self.result_view.display_results(event.name, results)
