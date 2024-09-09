from zabbix_utils import ZabbixAPI
from datetime import datetime
from sys import argv

"""Devuelve los ultimos 10 valores del item (tipo numero flotante) almacenado en el hitorial."""

item_id = argv[1] #Identificador del item

api = ZabbixAPI()

values = api.history.get(
    output=['clock', 'value'],
    history=0,
    itemids=item_id,
    sortfield="clock",
    limit=10,
    #sortorder="DESC",
)

for value in values:
    print(f"{datetime.fromtimestamp(int(value['clock'])).strftime('%Y/%m/%d %H:%M:%S')}", value['value'])
