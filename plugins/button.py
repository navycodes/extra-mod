################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


from pyrogram import *
from pyrogram.types import *
from telegraph import upload_file
from Userbot import *

__MODULES__ = "Button"


def help_string(org):
    return h_s(org, "help_button")


@ky.ubot("button")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    rep = m.reply_to_message or m
    teks = c.get_text(m)
    babi = await m.reply(_("proses").format(em.proses))
    id_button[c.me.id] = c.get_arg(m)
    if rep.text:
        dB.set_var(c.me.id, "id_button", id_button[c.me.id])
    elif rep.media:
        if rep.photo:
            file = rep.photo.file_id
            don = await c.download_media(file)
            oh = upload_file(don)
            mmk = f"https://telegra.ph/{oh[0]}"
            dB.set_var(c.me.id, "id_button_pic", mmk)
            dB.set_var(c.me.id, "id_button", id_button[c.me.id])
        elif rep.video:
            file = rep.video.file_id
            don = await c.download_media(file)
            oh = upload_file(don)
            mmk = f"https://telegra.ph/{oh[0]}"
            dB.set_var(c.me.id, "id_button_pic", mmk)
            dB.set_var(c.me.id, "id_button", id_button[c.me.id])
    text, keyboard = get_msg_button(teks)
    if keyboard:
        try:
            x = await c.get_inline_bot_results(
                bot.me.username, f"buat_button2 {c.me.id}"
            )
            await babi.delete()
            return await c.send_inline_bot_result(
                m.chat.id, x.query_id, x.results[0].id, reply_to_message_id=m.id
            )
        except Exception as e:
            return await babi.edit(_("err").format(em.gagal, e))

    else:
        await m.reply(_("butt_1").format(em.gagal))
        return await babi.delete()
