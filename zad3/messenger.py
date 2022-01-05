class TemplateEngine:
    def message(self, client , msg):
        pass

class MailServer:
    def send(self, client, msg):
        pass

    def receive(self, client):
        pass

class Messenger:
    def __init__(self) -> None:
        self.temp = TemplateEngine()
        self.server = MailServer()
    
    def send(self, msg, client):
        if isinstance(msg, str) and isinstance(client, str):
            self.server.send(self.temp.message(client, msg))
            return True
        raise ValueError
    
    def receive(self, client):
        if isinstance(client, str):
            self.server.receive(client)
            return True
        raise ValueError