## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME","BQA6uwpEeywkbsVwdpKapRUXqhUIPBy024SojP3SuiW48ixyPimSe-HOJxU0w26qjKi9MyQPq9lfQMYw1SVomKxX7y5hsOvvGtWOXlr8gw-BSIhe2KXcXTsS4I8pCgF4cJXPh2Ld-o3qSF9sANkuXqxPwYkyBVxwDNqAZnO-hfM68VKanN2Xoh62Ulq4R_9hsComdn1QSW1tw1rMmmi40bbPTrODNPgAiV4zsMbCXROLWTldWjGIT2n-j-tb6ODdctS8iJpIKUKDrPGeOwAtoMgeiqafmSBr-y26OKl5LRvJmgp3A8xJV-hyJM4GtBVDWt-5YMearfvUjSswkbbdPsHjAAAAAWWrTqgA")

if str(getenv("STRING_SESSION2")).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "6190665594:AAGMWBmYZjE0Aagiuw8yJNesCp0mANTltZI")
BOT_NAME = getenv("BOT_NAME", "SAMRAT x UTKARSH")

API_ID = int(getenv("API_ID", "29989697"))
API_HASH = getenv("API_HASH", "82ba29d96cc69cf153f1ce388299475b")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://pandeydatabase:Pandey2120@cluster0.pykk13g.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "Utkarsh")
OWNER_USERNAME = getenv("OWNER_USERNAME", "utkarshndharsh")
ALIVE_NAME = getenv("ALIVE_NAME", "Utkarsh")
BOT_USERNAME = getenv("BOT_USERNAME", "utkarsh_assistant_bot")
OWNER_ID = getenv("OWNER_ID", "5823840210")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "utkarsh_Assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "TheSupportChat")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TheUpdatesChannel")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1669178360").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ITZ-ZAID/Zaid-Vc-Player")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/10b1f781170b1e1867f68.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/6213d2673486beca02967.png")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
HEROKU_MODE = getenv("HEROKU_MODE", None)
