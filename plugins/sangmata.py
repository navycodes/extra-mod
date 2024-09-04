################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || Gojo_Satoru
"""
################################################################

import asyncio

from pyrogram import *
from pyrogram.errors import *
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.types import *
from Userbot import *

__MODULES__ = "SangMata"


def help_string(org):
    return h_s(org, "help_sg")


@ky.ubot("sg")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    puki = await c.extract_user(m)
    if len(m.command) < 2 and not m.reply_to_message:
        return await m.reply(_("sangmat_1").format(em.gagal))
    try:
        argu = (await c.get_users(puki)).id
    except UsernameInvalid:
        return await m.reply("{} Username invalid".format(em.gagal))
    except Exception:
        try:
            argu = int(m.command[1])
        except Exception as err:
            return await m.reply(_("err").format(em.gagal, err))
    except Exception as err:
        return await m.reply(_("err").format(em.gagal, err))
    proses = await m.reply(_("proses").format(em.proses))
    sg = "@SangMata_beta_bot"
    try:
        a = await c.send_message(sg, argu)
        await asyncio.sleep(1)
        await a.delete()
    except Exception as e:
        return await proses.edit(e)

    async for respon in c.search_messages(a.chat.id):
        if respon.text == None:
            continue
        if not respon:
            return await m.reply(_("sangmat_3").format(em.gagal))
        elif respon:
            await m.reply(_("sangmat_4").format(em.sukses, respon.text))
            break

    try:
        user_info = await c.resolve_peer(sg)
        await c.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))
    except Exception:
        pass

    return await proses.delete()
