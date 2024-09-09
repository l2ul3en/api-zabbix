class Hostgroup:

    def __init__(self, groupid: int, name: str):
        self.groupid = int(groupid)
        self.name = name
    
    def __repr__(self) -> str:
        return f"Hostgroup(groupid={self.groupid}, name={self.name})"