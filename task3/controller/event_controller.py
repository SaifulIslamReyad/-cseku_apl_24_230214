class EventController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def start_event(self):
        return self.view.display_event_start(self.model.name)
