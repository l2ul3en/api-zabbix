from zabbix_utils import ZabbixAPI

api = ZabbixAPI()

users = api.hostgroup.get(
    output=['name']
)

for user in users:
    print(user['name'])
