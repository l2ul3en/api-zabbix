from os import environ
import tomllib

class Config:

    try:
        TOKEN = environ["ZABBIX_TOKEN"]
        URL = environ["ZABBIX_URL"]
    except KeyError as e:
        raise RuntimeError("Could not found ZABBIX_TOKEN or ZABBIX_URL in environment") from e
    
    FILE_CONFIG = 'config.toml' 
    try:
        with open(FILE_CONFIG, 'rb') as conf:
            DATA = tomllib.load(conf)
    except tomllib.TOMLDecodeError as e:
        raise RuntimeError(f"Invalid TOML document {FILE_CONFIG}") from e
