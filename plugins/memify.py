################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || MIKIR GOBLOK, TOLOL, IDIOT, NGENTOT, KONTOL, BAJINGAN
  • JANGAN DIHAPUS YA MONYET-MONYET SIALAN
"""
################################################################

from Userbot import *

__MODULES__ = "Memify"


def help_string(org):
    return h_s(org, "help_mmf")


@ky.ubot("mmf|memify")
async def memify(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    rep = m.reply_to_message
    pros = await m.reply(_("proses").format(em.proses))
    if not rep and not rep.media:
        await pros.edit(_("mmf_1").format(em.gagal))
        return
    txt = c.get_arg(m)
    if not txt:
        return await pros.edit(_("mmf_1").format(em.gagal, m.text.split()[0]))
    doc = await c.download_media(rep)
    meme = await add_text_img(doc, txt)
    await asyncio.gather(
        pros.delete(),
        c.send_sticker(
            m.chat.id,
            sticker=meme,
            reply_to_message_id=ReplyCheck(m),
        ),
    )
    os.remove(meme)
    return
