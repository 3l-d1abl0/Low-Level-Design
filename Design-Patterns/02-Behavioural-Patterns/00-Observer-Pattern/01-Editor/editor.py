from abc import ABC, abstractmethod

class EventListener(ABC):

    @abstractmethod
    def update(self, event_type: str, file):
        pass

class EventManager:

    def __init__(self, event_types):
        self.operations = event_types
        self.listeners = {}

        for event_type in self.operations:
            self.listeners[event_type] =[]

    def subscribe(self, event_type: str, listeners: EventListener):

        users = self.listeners[event_type]
        users.append(listeners)

    def unsubscribe(self, event_type: str, listeners: EventListener):

        users = self.listeners[event_type]
        users.remove(listeners)

    def notify(self, event_type, file):
        users = self.listeners[event_type]
        for u in users:
            u.update(event_type, file)



class Editor:

    events = EventManager(["open", "close"])
    file = None

    def open_file(self, file):
        self.file = file

        print(f"Editor: opening file{file}")
        self.events.notify("open", file)

    def close_file(self):
        print(f"Editor: closing file {self.file}")
        self.events.notify("close", self.file)


class EmailNotificationListener(EventListener):
    def __init__(self, email):
        self.email = email

    def update(self, event_type: str, file):
        print(f"Email to {self.email}: Someone has performed {event_type} operation on the file {file}")

class LogOpenListener(EventListener):
    def __init__(self, log_file):
        self.log_file = log_file

    def update(self, event_type: str, file):
        print(f"Save to Log {self.log_file}: Someone has performed {event_type} operation on the file {file}")



if __name__ == "__main__":

    editor = Editor()


    email_listener = EmailNotificationListener("test@gmail.com")
    log_listener = LogOpenListener("path/to/log/file.txt")


    editor.events.subscribe("open", log_listener)
    editor.events.subscribe("close", log_listener)
    editor.events.subscribe("close", email_listener)


    editor.open_file("newFile.txt")
    editor.close_file()
