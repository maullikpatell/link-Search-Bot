# (c) @AM_ROBOTS

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "LinkSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    DATABASE_URL = os.environ.get("DATABASE_URL")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Link Search Bot.
    
    
    
🤖 My Name: <a href='https://t.me/DTG_BOTS'>DTG LINKS BOT</a>
📝 Language : <a href='https://www.python.org'> Python V3</a>
📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>
📡 Server: <a href='https://railway.app'>Railway</a>
👨‍💻 Created By: <a href='https://t.me/DTG_BOTS'>DTG BOTS</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Developer : <a href='https://t.me/DTG_ADMIN_BOT'>Click Me</a>
If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm DTG LINKS BOT.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With 🔥 @DTG_BOTS</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm DTG LINKS BOT.🤖</a>

I Can Search 🔍 What You Want❗

<a>Made With 🔥 @DTG_BOTS</a></b>
"""

