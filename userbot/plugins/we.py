from . import reply_id

WPIC = "https://telegra.ph/file/dfd7fc05a81748a87761c.jpg"

@bot.on(admin_cmd(pattern="م21"))
async def wspr(kimo):
  await kimo.edit(
  "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑺𝑬𝑪𝑹𝑬𝑻 𝑴𝑺𝑮 𓆪\n"
  "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
  "**⌔∮ قائـمه اوامر الهمسه :** \n"
  "⪼ `.همسه` لعرض كيفيه ارسال همسه \n"
  "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
  "𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝙞𝘾𝙎𝙎 - [𝘿𝙀𝙑](t.me/rruuurr) 𓆪"
  )
    

from . import reply_id
from .IcssGif import *

@bot.on(admin_cmd(outgoing=True, pattern="ت2$"))
async def tmgif(lon):
    if lon.fwd_from:
        return
    lonid = await reply_id(lon)
    if WPIC:
        ics_c = f"@bot_username secret @NIIIN2 الرساله\n"
        ics_c += f"اذا تريد ترسل همسه من خلال البوت الخاص بك يجب كتابه اولا #معرف_البوت ثم #secret ثم تكتب #معرف_الي_تريد_تهمسله ثم #الرساله وستضهر ايقونه وتضغط عليها وبس 🖤✨."
        await lon.client.send_file(lon.chat_id, WPIC, caption=ics_c, reply_to=lonid)
