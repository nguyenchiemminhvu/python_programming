from abc import ABC, abstractmethod
import time

class notifier(ABC):
    @abstractmethod
    def notify(self, message: str):
        pass

class base_notifier(notifier):
    def notify(self, message: str):
        print(f"Notification: {message}")

class email_notifier(notifier):
    def __init__(self, notifier: notifier):
        self._notifier = notifier
    
    def notify(self, message: str):
        self._notifier.notify(message)
        print(f"Sending email with message: {message}")

class sms_notifier(notifier):
    def __init__(self, notifier: notifier):
        self._notifier = notifier
    
    def notify(self, message: str):
        self._notifier.notify(message)
        print(f"Sending SMS with message: {message}")

class push_notifier(notifier):
    def __init__(self, notifier: notifier):
        self._notifier = notifier
    
    def notify(self, message: str):
        self._notifier.notify(message)
        print(f"Sending push notification with message: {message}")

class application:
    def __init__(self, notifier: notifier):
        self._notifier = notifier
    
    def run(self):
        try:
            while (True):
                self.send_notification("Hello, this is a notification!")
                time.sleep(1)
        except KeyboardInterrupt:
            print()
            print("Application stopped.")

    def send_notification(self, message: str):
        self._notifier.notify(message)

if __name__ == "__main__":
    base = base_notifier()
    email = email_notifier(base)
    sms = sms_notifier(email)
    push = push_notifier(sms)

    app = application(push)
    app.run()