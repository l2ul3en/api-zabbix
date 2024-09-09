import re, sys

def validar_formato(cad:str, patron:str)-> bool:
    regexp = re.compile(patron, re.IGNORECASE)
    return bool(regexp.match(cad))

def _get_regexp(cad:str, sep:str)-> str:
    return cad.split(sep)

def _existe_mac(macs:list, mac: str)-> bool:
    #regexp = re.compile(r'([A-F0-9]{12})', re.IGNORECASE)
    for i in macs:
        #if (matches := regexp.search(mac).group(1)) == mac:
        if i.lower() == mac.lower():
            print(f"la mac {mac!r} ya existe en la macro {i!r}")
            return True
    return False

def append_expresion(cad: str, new_mac: str) -> str:
    regexp = re.compile(r'CM-\((.*)\)')
    #matches = regexp.match(cad)
    if matches := regexp.match(cad):
        print("match expresion: ", regexp.pattern , "->", matches.string)
        lista_macs = _get_regexp(matches.group(1),'|')
        if not _existe_mac(lista_macs, new_mac):
            lista_macs.append(new_mac)
            new_macro = '|'.join(lista_macs)
            return f"CM-({new_macro})"

if __name__ == '__main__':
    v = sys.argv[1]
    append_expresion(v)
