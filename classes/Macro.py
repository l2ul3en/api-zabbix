from classes.ApiObject import ApiObject
class Macro(ApiObject):
    def __init__(self):
        super().__init__()

    def __init__(self, hostmacroid: int = 0, hostid: int = 0, macro: str = "", \
value: str = "", description: str = "", type: int = 0, automatic: int = 0):
        self.hostmacroid = hostmacroid
        self.hostid = int(hostid)
        self.macro = macro
        self.value = value
        self.description = description
        self.type = int(type)
        self.automatic = int(automatic)
        super().__init__() 

    def cargar_data(self, hostid: int):
        return [Macro(**i) for i in self.get_usermacros(hostid)]

    def __repr__(self) -> str:
        return f"Macro(hostmacroid={self.hostmacroid}, hostid={self.hostid}, macro={self.macro}, value={self.value}, \
description={self.description}, type={self.type}, automatic={self.automatic})"
