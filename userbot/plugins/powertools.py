import sys
from os import execl
from time import sleep

from . import BOTLOG, BOTLOG_CHATID, HEROKU_APP, bot


@bot.on(admin_cmd(pattern="اعادة تشغيل$"))
@bot.on(sudo_cmd(pattern="اعادة تشغيل$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID, "#اعادة_التشغيل \n" "⪼ بوت اكسس في وضع اعادة التشغيل انتظر"
        )
    await edit_or_reply(
        event,
        "**اعادة التشغيل** ↫ استخدم `.ايدي` او `.بنك` للتحقق مما إذا كنت متصلاً بالإنترنت ، يستغرق الأمر في الواقع 1-2 دقيقة لإعادة التشغيل",
    )
    await bot.disconnect()
    execl(sys.executable, sys.executable, *sys.argv)


@bot.on(admin_cmd(pattern="ايقاف$"))
@bot.on(sudo_cmd(pattern="ايقاف$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID, "#اطفاء \n" "بوت اكسس في وضع الاطفاء"
        )
    await edit_or_reply(
        event, "**جارٍ إيقاف تشغيل بوت اكسس الآن ... شغِّلني يدويًا لاحقًا**"
    )
    if HEROKU_APP is not None:
        HEROKU_APP.process_formation()["userbot"].scale(0)
    else:
        sys.exit(0)


CMD_HELP.update(
    {
        "powertools": "**Plugin : **`powertools`\
        \n\n  •  **Syntax : **`.restart`\
        \n  •  **Function : **__Restarts the bot !!__\
        \n\n  •  **Syntax : **`.sleep <seconds>`\
        \n  •  **Function: **__Userbots get tired too. Let yours snooze for a few seconds.__\
        \n\n  •  **Syntax : **`.shutdown`\
        \n**  •  Function : **__To turn off the dyno of heroku. you cant turn on by bot you need to got to heroku and turn on or use__ @hk_heroku_bot"
    }
)
