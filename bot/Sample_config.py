import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5533113564:AAGszACC2lzfkjiWbppFL-qMZ86jtp7ryVY")
    API_ID = int(os.environ.get("API_ID", 17795696))
    API_HASH = os.environ.get("API_HASH", "afcbcd249c7d8728d9b213b10d39a649")
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "Pytogram_support")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Emlifhbot")
