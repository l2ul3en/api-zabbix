from sys import argv
from classes.Macro import Macro
from classes.Host import Host
from datetime import datetime
import utils.tools as ut

myhostid, ip, macro, user, mac = argv[1].split('|')
myhostid = int(myhostid)

obj = Macro()
assert ut.validar_formato(mac, r'^([A-F0-9]{12})$'), "La nueva mac no tiene el formato correcto"

if obj.existe_usermacro(myhostid, macro):
    #update macro
    buscado = Macro(**obj.get_usermacro(myhostid, macro)[0])
    new_value = ut.append_expresion(buscado.value, mac)
    if new_value:
        aux = obj.set_usermacro(buscado.hostmacroid, new_value)
        print("usermacro actualizada",new_value)
else:
    #cree la macro
    obj.create_usermacro(myhostid, macro, f"CM-({mac})")
    print(f"usermacro creada en {myhostid}")

dt = datetime.now()
item = obj.create_item_cm_dead_date(
    u_name= f"{mac}: CM Datetime of dead",
    u_key= f"cm.date_dead[{mac}]",
    u_hostid= myhostid,
    u_type= 21,  ##Script 
    u_value_type= 4, ##Text
    u_delay= "10m",
    u_params= f"return {dt.strftime('%Y%m%d %H%M%S')!r};", #Content of script
    u_tags= [{"tag": "component", "value": "cm-seguimiento"}],
    u_preprocessing= [{"type": 19}]
)
print("Item creado", item['itemids'][0])

host = Host()
my_ob = host.cargar_data(myhostid)[0]
print(my_ob)

trigger = obj.create_trigger_cm_check_dead_date(
    u_description = f"{mac}: Eliminar CM seguimiento",
    u_expression = f"date() >= left(last(/{my_ob.host}/cm.date_dead[{mac}]),8) and time() >= right(last(/{my_ob.host}/cm.date_dead[{mac}]),6)",
    u_priority = 1, #Information
    u_tags = [{"tag": "performance", "value": "cm-seguimiento"}],
)
print("Trigger creado", trigger['triggerids'][0])
