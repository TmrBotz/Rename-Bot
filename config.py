import os



# Required Variables Config
API_ID = int(os.environ.get("API_ID", "23171051"))
API_HASH = os.environ.get("API_HASH", "10331d5d712364f57ffdd23417f4513c")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7473136514:AAFz5Aemf6r4SznohWwmX6Vr5_QjaCUp8Y8")
ADMIN = int(os.environ.get("ADMIN", "6987799874"))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "Tmr_Botz")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002205504138"))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://drozmarizabel991hull:Xh89XLrFTYOPgupl@cluster0.x8qoe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Ana")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/ada3f739fed7efdbe7b08.jpg")
