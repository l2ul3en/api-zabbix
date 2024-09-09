from classes.Host import Host
class Event:

    def __init__(self, eventid: int, value: int, hosts: list):
        self.eventid = int(eventid)
        self.value = int(value)
        self.hosts = Host(**hosts[0])
    
    def __repr__(self) -> str:
        return f"Event(eventid={self.eventid}, value={self.value}, hosts={self.hosts})"