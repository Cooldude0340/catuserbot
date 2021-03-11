########################  SOURCE ICSS ~ BY: KIMO (@RRUUURR)  ########################


import time

from . import StartTime, get_readable_time, reply_id

DEFAULTUSER = "ICSS"
CAT_IMG = "https://telegra.ph/file/6e707dc14cb918cd765fb.mp4"
CUSTOM_ICSS_TEXT = "𓆩𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑻𝑼𝑴𝑩𝑳𝑹 𝑮𝑰𝑭𓆪"
EMOJI = "  ↫ "


@bot.on(admin_cmd(outgoing=True, pattern="ت2$"))
@bot.on(sudo_cmd(pattern="ت2$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    await get_readable_time((time.time() - StartTime))
    if CAT_IMG:
        cat_caption = f"**{CUSTOM_ICSS_TEXT}**\n"
        cat_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        cat_caption += f"**↫ المتـحركه الثانيه 𓆰.**"
        await alive.client.send_file(
            alive.chat_id, CAT_IMG, caption=cat_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ICSS_TEXT}**\n"
            f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
            f"**↫ المتـحركه الثانيه 𓆰.**",
        )
