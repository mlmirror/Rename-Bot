# (c) @AbirHasan2005

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    API_ID = int(os.environ.get("API_ID", "29451274"))
    API_HASH = os.environ.get("API_HASH", "b31187ad9698e1858ecfc71c96123d55")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6313327011:AAEEwHy4XaVv8RUOS0Kg30ld6SnvOU2ZQwQ")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("OWNER_ID", 1945723944)
    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "0").split()))
    PRO_USERS.append(OWNER_ID)
    MONGODB_URI = os.environ.get("MONGODB_URI", "https://cloud.mongodb.com/v2/63cc1e24ba9efa06ab78ae22#/clusters/detail/niho")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-100804903352"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
