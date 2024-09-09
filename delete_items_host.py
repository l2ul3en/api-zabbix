from zabbix_utils import ZabbixAPI
from sys import argv

"""Devuelve los items asociados al host."""

#host_id = argv[1] #Identificador de host

api = ZabbixAPI()

items = api.item.delete(
   params = ['46894', '46899', '46900'],
)

print(items)
