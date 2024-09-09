from zabbix_utils import ZabbixAPI
from sys import argv

"""Devuelve los items asociados al host."""

host_id = argv[1] #Identificador de host

api = ZabbixAPI()

items = api.item.get(
    output=['itemid', 'name'],
    hostids=host_id,
    #search= {"key_":"icmp"}
    search= {"name":"*name"},
    searchWildcardsEnabled="true"
)

for item in items:
    print(item['itemid'], item['name'])
