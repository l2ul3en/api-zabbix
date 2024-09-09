from zabbix_utils import ZabbixAPI
from utils.vars import Config


class ApiObject:

    def __init__(self):
        self.api = ZabbixAPI(url=Config.URL)
        self.api.login(token=Config.TOKEN)

    def get_all_problems(self):
        problems = self.api.problem.get(
            output = ["objectid",  "eventid", "severity", "name", "acknowledged", "clock", "r_clock"],
            recent = True,
            sortfield = "eventid",
            sortorder = "ASC",
        )
        return problems
    
    def get_event(self, eventid: int):
        events = self.api.event.get(
            output = ["eventid", "value"],
            eventids = eventid,
            selectHosts = ["host","name", "description"],
            sortorder = "DESC",
        )
        return events
    
    def get_groups(self, hostid: int):
        groups = self.api.hostgroup.get(
            output = ["name","groupid"],
            hostids = hostid,
        )
        return groups
    
    def existe_usermacro(self, hostid: int, macro: str):
        """Returns true if exist one usermacro."""
        return int(self.api.usermacro.get (
                hostids = hostid,
                countOutput = True,
                search = {
                    "macro" : macro,
                },
            )
        ) >= 1

    def get_usermacros(self, hostid: int):
        """Returns all usermacros of one host."""
        macros = self.api.usermacro.get(
            hostids = hostid,
        )
        return macros

    def get_usermacro(self, hostid: int, user_macro: str):
        """Returns an usermacro of one host."""
        macro = self.api.usermacro.get(
            hostids = hostid,
            filter = {
                "macro" : user_macro,
            },
        )
        return macro

    def set_usermacro(self, user_hostmacroid: int, user_value: str):
        """Update the value of the usermacro."""
        self.api.usermacro.update(
            hostmacroid = user_hostmacroid,
            value = user_value,
        )

    def create_usermacro(self, user_hostid: int, user_macro: str, user_value: str, user_description="Macro creada con API"):
        """Create one usermacro on the specific host."""
        ob = self.api.usermacro.create(
            hostid = user_hostid,
            macro = user_macro,
            value = user_value,
            description = user_description,
        )
        return ob
    
    def create_item_cm_dead_date(self, u_name:str, u_key:str, u_hostid:int, u_type:int, \
u_value_type:int, u_delay:str, u_params:str, u_tags:list, u_preprocessing:list):
        """Create one item on specific host."""
        item = self.api.item.create(
            name = u_name,
            key_ = u_key,
            hostid = u_hostid,
            type = u_type,
            value_type = u_value_type,
            delay = u_delay,
            params = u_params,
            tags = u_tags,
            preprocessing = u_preprocessing
        )
        return item

    def create_trigger_cm_check_dead_date(self, u_description:str, u_expression:str, u_priority:int, u_tags:list):
        """Create one trigger on specific host."""
        trigger = self.api.trigger.create(
            description = u_description,
            expression = u_expression,
            priority = u_priority,
            tags = u_tags,
        )
        return trigger

    def get_host(self, hostid:int):
        """Return one host."""
        host = self.api.host.get(
            output = "extend",
            hostids = hostid,
        )
        return host
