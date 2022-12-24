from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 28533415
API_HASH = "96332cd303a9277980b5dd0274568b36"
BOT_TOKEN = "5882308938:AAFfDSzIARrQsN6Lf_-GoDZPv4Vfs5xHVvI"
BOT_UN = "For_Batak"

Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
