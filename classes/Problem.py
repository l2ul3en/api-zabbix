class Problem:

    def __init__(self, eventid: int, objectid: int, severity: int, 
                name: str, acknowledged: int, clock: int, r_clock:int):
        self.eventid = int(eventid)
        self.objectid = int(objectid)
        self.severity = int(severity)
        self.name = name
        self.acknowledged = int(acknowledged)
        self.clock = int(clock)
        self.r_clock = int(r_clock)

    def __repr__(self) -> str:
        return f"Problem(objectid={self.objectid}, eventid={self.eventid}, severity={self.severity}, name={self.name}, acknowledged={self.acknowledged}, clock={self.clock}, r_clock={self.r_clock})"