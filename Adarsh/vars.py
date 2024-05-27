# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', "25976580"))
    API_HASH = str(getenv('API_HASH', "b5562ab77a96e49bc9dd78cc103c6333"))
    BOT_TOKEN = str(getenv('BOT_TOKEN', "7167598037:AAH6u2km_8i0fa4o7ZurhCBxpZYLn6DS1VQ"))
    name = str(getenv('name', 'filetolinkbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', "-1002230004176"))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "6708929009").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = str(getenv('APP_NAME'))
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', "UmmBaby"))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "0.tcp.ap.ngrok.io ".format(FQDN)
    else:
        URL = "19278".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', "mongodb+srv://developervro:developerrapuka@cluster9.gcj9754.mongodb.net/?retryWrites=true&w=majority&appName=Cluster9"))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', "jsjsjks"))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) 
