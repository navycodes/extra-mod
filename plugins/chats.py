
import asyncio

from Userbot import *

__MODULES__ = "Chats"


def help_string(org):
    return h_s(org, "help_cc")
    
    

@ky.ubot("cekmember")
async def _(c, m, _):
    em = Emojik(c)
    em.initialize()
    chat_id = m.command[1] if len(m.command) > 1 else m.chat.id
    pros = await m.reply(_("proses").format(em.proses))
    try:
        o = await c.get_chat_members_count(chat_id)
        await asyncio.sleep(1)
        return await pros.edit("{} Total members group {}".format(em.sukses, o))
    except Exception as e:
        return await pros.edit(_("err_1").format(em.gagal, str(e)))
        
        
@ky.ubot("cekonline")
async def _(c, m, _):
    em = Emojik(c)
    em.initialize()
    chat_id = m.command[1] if len(m.command) > 1 else m.chat.id
    pros = await m.reply(_("proses").format(em.proses))
    try:
        o = await c.get_chat_online_count(chat_id)
        await asyncio.sleep(1)
        return await pros.edit("{} Total members online group {}".format(em.sukses, o))
    except Exception as e:
        return await pros.edit(_("err_1").format(em.gagal, str(e)))
        
        
@ky.ubot("cekmsg")
async def _(c, m, _):
    em = Emojik(c)
    em.initialize()
    chat_id = m.command[1] if len(m.command) > 1 else m.chat.id
    user_id = await c.extract_user(m)
    if not user_id:
        return await m.reply_text(_("glbl_2").format(em.gagal))
    try:
        umention = (await c.get_users(user_id)).mention
    except (PeerIdInvalid, KeyError):
        return await m.reply_text(_("peer").format(em.gagal))
    pros = await m.reply(_("proses").format(em.proses))
    try:
        o = await c.search_messages_count(chat_id, from_user=user_id)
        await asyncio.sleep(1)
        return await pros.edit("{} Total message from user {} is {} messages".format(em.sukses, umention, o))
    except Exception as e:
        return await pros.edit(_("err_1").format(em.gagal, str(e)))