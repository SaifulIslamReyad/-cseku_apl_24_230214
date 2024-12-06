class RegistrationController:
    def __init__(self, registration_model, participant_view):
        self.registration_model = registration_model
        self.participant_view = participant_view

    def register_participant(self, participant, event):
        self.registration_model.register_participant(participant, event)
        return self.participant_view.display_registration(participant.name, event.name)
