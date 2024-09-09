from zabbix_utils import ZabbixAPI

api = ZabbixAPI()

hosts = api.host.get(
    output="extend"
    #output=['hostid', 'name']
)

for host in hosts:
    #print(host['hostid'], host['name'])
    #print(type(host))
    for key in host.keys():
#    print(host['hostid'], host['name'])
        print(key, host[key])
