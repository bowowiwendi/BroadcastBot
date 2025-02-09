import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7632200131:AAGZ7x_Ih1Uxu0gx2qbhYr-IO1DrZhJtL8o")
API_ID = int(os.environ.get("API_ID", "5162695441"))
API_HASH = os.environ.get("API_HASH", "")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "BroadcastBot")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
