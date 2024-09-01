################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


import os

from Userbot import *

__MODULES__ = "Curi"


def help_string(org):
    return h_s(org, "help_spy")


@ky.ubot("curi|spy")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    dia = m.reply_to_message
    if not dia:
        return
    gclog = c.get_logger(c.me.id)
    logs = gclog if gclog else "me"
    anjing = dia.caption or ""
    await m.delete()

    if dia.photo or dia.video or dia.audio or dia.voice or dia.document:
        anu = await c.download_media(dia)

        if os.path.getsize(anu) == 0:
            os.remove(anu)
            await c.send_message(logs, _("spy_1").format(em.gagal))
            return

        try:
            if dia.photo:
                await c.send_photo(logs, anu, anjing)
            elif dia.video:
                await c.send_video(logs, anu, anjing)

            elif dia.audio:
                await c.send_audio(logs, anu, anjing)

            elif dia.voice:

                await c.send_voice(logs, anu, anjing)

            elif dia.document:

                await c.send_document(logs, anu, anjing)
        except Exception as e:

            await c.send_message(logs, _("err").format(em.gagal, e))

        finally:
            os.remove(anu)
    else:

        await c.send_message(logs, _("spy_2").format(em.sukses))
        return
