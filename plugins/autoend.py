import asyncio

from pyrogram.errors import *
from pyrogram.raw.functions.messages import DeleteHistory
from Userbot import *

__MODULES__ = "ClearChat"


def help_string(org):
    return h_s(org, "help_cc")


@ky.ubot("cc")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    reply = m.reply_to_message
    if reply and reply.sender_chat and reply.sender_chat != m.chat.id:
        aan = await m.reply_text(_("res_3").format(em.gagal))
        await asyncio.sleep(0.5)
        return await aan.delete()
    if len(m.command) == 2:
        user = m.text.split(None, 1)[1]
    elif len(m.command) == 1 and reply:
        user = m.reply_to_message.from_user.id
    else:
        aa = await m.reply_text(_("prof_1").format(em.gagal))
        await asyncio.sleep(0.5)
        return await aa.delete()
    await m.delete()
    try:
        return await c.delete_user_history(m.chat.id, user)
    except:
        pass


@ky.ubot("clearchat|endchat|clchat")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    rep = m.reply_to_message
    mek = await m.reply(_("proses").format(em.proses))
    if len(m.command) < 2 and not rep:
        await m.reply(_("auend_1").format(em.gagal))
        return
    if len(m.command) == 1 and rep:
        who = rep.from_user.id
        try:
            info = await c.resolve_peer(who)
            await c.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
        except PeerIdInvalid:
            pass
        await m.reply(_("auend_2").format(em.sukses, who))
    else:
        if m.command[1].strip().lower() == "all":
            biji = await c.get_chats_dialog("usbot")
            for kelot in biji:
                try:
                    info = await c.resolve_peer(kelot)
                    await c.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
                except PeerIdInvalid:
                    continue
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                    info = await c.resolve_peer(kelot)
                    await c.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
            await m.reply(_("auend_3").format(em.sukses, len(biji)))
        elif m.command[1].strip().lower() == "bot":
            bijo = await c.get_chats_dialog("bot")
            for kelot in bijo:
                try:
                    info = await c.resolve_peer(kelot)
                    await c.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
                except PeerIdInvalid:
                    continue
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                    info = await c.resolve_peer(kelot)
                    await c.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
            await m.reply(_("auend_4").format(em.sukses, len(bijo)))
        else:
            who = m.text.split(None, 1)[1]
            try:
                info = await c.resolve_peer(who)
                await c.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
            except PeerIdInvalid:
                pass
            except FloodWait as e:
                await asyncio.sleep(e.value)
                info = await c.resolve_peer(who)
                await c.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
            await m.reply(_("auend_2").format(em.sukses, who))
    await mek.delete()
    return
