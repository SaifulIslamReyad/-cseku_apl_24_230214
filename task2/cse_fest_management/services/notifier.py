from interfaces.notification_interface import NotificationInterface

class Notifier(NotificationInterface):
    def notify_participant(self, participant, message):
        print(f"Notification to {participant.name}: {message}")