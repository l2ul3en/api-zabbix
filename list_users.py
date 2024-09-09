from zabbix_utils import ZabbixAPI

api = ZabbixAPI()

users = api.user.get(
    output=['username']
)

for user in users:
    print(user['username'])
