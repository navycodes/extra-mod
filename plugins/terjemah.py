################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

import os

import gtts
from config import *
from gpytranslate import Translator
from Userbot import *
from Userbot.helper.database import *
from Userbot.helper.langs import *

__MODULES__ = "Translate"


def help_string(org):
    return h_s(org, "help_terjemah")


@ky.ubot("tts")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    pros = await m.reply(_("proses").format(em.proses))
    if m.reply_to_message:
        bhs = c._translate[c.me.id]["negara"]
        kata = m.reply_to_message.text or m.reply_to_message.caption
    else:
        if len(m.command) < 2:
            await pros.edit(_("tr_1").format(em.gagal, m.command))
        else:
            bhs = c._translate[c.me.id]["negara"]
            kata = m.text.split(None, 1)[1]
    gts = gtts.gTTS(kata, lang=bhs)
    gts.save("trs.oog")
    rep = m.reply_to_message or m
    try:
        await c.send_voice(
            chat_id=m.chat.id,
            voice="trs.oog",
            reply_to_message_id=rep.id,
        )
        await pros.delete()
        os.remove("trs.oog")
        return
    except Exception as er:
        await pros.edit(_("err").format(em.gagal, er))
        return
    except FileNotFoundError:
        pass


@ky.ubot("tr")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    trans = Translator()
    pros = await m.reply(_("proses").format(em.proses))
    if m.reply_to_message:
        bhs = c._translate[c.me.id]["negara"]
        txt = m.reply_to_message.text or m.reply_to_message.caption
        src = await trans.detect(txt)
    else:
        if len(m.command) < 2:
            await m.reply(_("tr_1").format(em.gagal, m.command))
            return
        else:
            bhs = c._translate[c.me.id]["negara"]
            txt = m.text.split(None, 1)[1]
            src = await trans.detect(txt)
    trsl = await trans(txt, sourcelang=src, targetlang=bhs)
    reply = _("tr_2").format(em.sukses, trsl.text)
    rep = m.reply_to_message or m
    await pros.delete()
    await c.send_message(m.chat.id, reply, reply_to_message_id=rep.id)
    return


@ky.ubot("lang")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    try:
        bhs_list = "\n".join(
            f"- **{lang}**: `{code}`" for lang, code in kode_bahasa.items()
        )
        await m.reply(_("tr_3").format(em.sukses, bhs_list))
        return
    except Exception as e:
        await m.reply(_("err").format(em.gagal, e))
        return


@ky.ubot("setlang")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    pros = await m.reply(_("proses").format(em.proses))
    if len(m.command) < 2:
        await pros.edit(_("tr_4").format(em.gagal, m.text))
        return
    for lang, code in kode_bahasa.items():
        kd = m.text.split(None, 1)[1]
        if kd.lower() == code.lower():
            c._translate[c.me.id] = {"negara": kd}
            await pros.edit(_("tr_5").format(em.sukses, kd, lang))
            return
    await pros.edit(_("tr_6").format(em.gagal))
    return
