from classes.ApiObject import ApiObject

class Host(ApiObject):

    def __init__(self):
        super().__init__()

    def __init__(self, hostid: int=0, proxyid:int=0, host: str='', status:int=0, ipmi_authtype:int=0, ipmi_privilege:int=0,\
ipmi_username:str='', ipmi_password:str='', maintenanceid:int=0, maintenance_status:int=0, maintenance_type:int=0, maintenance_from:int=0, name: str='', flags:int=0, templateid:int=0, description:str='',\
tls_connect:int=0, tls_accept:int=0, tls_issuer:str='', tls_subject:str='', custom_interfaces:int=0, uuid:str='', vendor_name:str='',\
vendor_version:str='', proxy_groupid:int=0, monitored_by:int=0, inventory_mode:int=0, active_available:int=0, assigned_proxyid:int=0):
        self.hostid = int(hostid)
        self.proxyid = int(proxyid)
        self.host = host
        self.status = int(status)
        self.ipmi_authtype = int(ipmi_authtype)
        self.ipmi_privilege = int(ipmi_privilege)
        self.ipmi_username = ipmi_username
        self.ipmi_password = ipmi_password
        self.maintenanceid = maintenanceid
        self.maintenance_status = int(maintenance_status)
        self.maintenance_type = int(maintenance_type)
        self.maintenance_from = int(maintenance_from)
        self.name = name
        self.flags = flags
        self.templateid = int(templateid)
        self.description = description
        self.vendor_version = vendor_version
        self.proxy_groupid = int(proxy_groupid)
        self.monitored_by = int(monitored_by)
        self.inventory_mode = int(inventory_mode)
        self.active_available = int(active_available)
        self.assigned_proxyid = int(assigned_proxyid)
        super().__init__()

    def cargar_data(self, hostid: int):
        return [Host(**i) for i in self.get_host(hostid)]

    def __repr__(self) -> str:
        return f"Host(hostid={self.hostid}, host={self.host}, name={self.name}, description={self.description})"
