سimport glob
import os
import sys
from pathlib import Path

import telethon.utils
from telethon import TelegramClient

from . import LOGS, bot
from .Config import Config
from .utils import load_module


async def add_bot(bot_token):
    try: 
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        LOGS.error(f"STRING_SESSION - {str(e)}")
        sys.exit()


if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try: 
        if Config.TG_BOT_USERNAME is not None:
            LOGS.info("⫷ جاري تنزيل انلاين البوت ⫸")
            # ForTheGreatrerGood of beautification
            bot.tgbot = TelegramClient(
                "TG_BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH
            ).start(bot_token=Config.TG_BOT_TOKEN)
            LOGS.info("⫷ تم تنزيل انلاين بدون اخطاء ⫸")
            LOGS.info("⫷ جاري بدء بوت اكسس ⫸")
            bot.loop.run_until_complete(add_bot(Config.TG_BOT_USERNAME))
            LOGS.info("⫷ تم بدء بوت اكسس ⫸")
        else:
            bot.start()
     except Exception as e:
         LOGS.error(f"TG_BOT_TOKEN - {srt(e)}")
         sys.exit()

path = "userbot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        try: 
            if shortname.replace(".py", "") not in Config.NO_LOAD:
                load_module(shortname.replace(".py", ""))
            else: 
                os.remove(Path(f"userbot/plugins/{shortname}.py"))
        except Exception as e:
           os.remove(Path(f"userbot/plugins/{shortname}.py))
           LOGS.info(f"⫷ لا يمكن تحميل {shortname} بسبب الخطأ {e} ⫸")

LOGS.info("⫷ بوت اكسس يعمل بنجاح ⫸")
LOGS.info(
    "⫷ مبروك عزيزي اكتب الان .ايدي لترى ما اذا كان البوت يعمل ⫸\
    \n ⫷ إذا كنت بحاجة إلى مساعدة ، فتوجه إلى مطورس السورس https://t.me/rruuurr ⫸"
)


async def startupmessage():
    try:
        if Config.PRIVATE_GROUP_BOT_API_ID != 0:
            await bot.send_message(
                Config.PRIVATE_GROUP_BOT_API_ID,
                "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺  - 𝑼𝑷𝑫𝑨𝑻𝑬 𝑴𝑺𝑮 ⤵︎\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n**⪼ مبروك عزيزي اكتب الان .ايدي لترى ما اذا كان بوت اكسس يعمل**\
        \n ⪼ إذا كنت بحاجة إلى مساعدة راسل مطوري\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆰 𝙎𝙊𝙐𝙍𝘾𝞝 𝙄𝘾𝙎𝙎 - [𝘿𝙀𝙑](t.me/rruuurr)  𓆪",
                link_preview=False,
            )
    except Exception as e:
        LOGS.info(str(e))


bot.loop.create_task(startupmessage())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()

