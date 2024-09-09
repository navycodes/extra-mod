################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

import asyncio

from pyrogram.enums import ChatType
from pyrogram.errors import (ChatForwardsRestricted, FloodWait,
                             MessageIdInvalid, PeerFlood, UserRestricted)
from Userbot import *

__MODULES__ = "Gruplog"


def help_string(org):
    return h_s(org, "help_gruplog")


@ky.ubot("gruplog")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    xx = await m.reply(_("proses").format(em.proses))
    cek = c.get_arg(m)
    if cek.lower() == "on":
        if not dB.get_var(c.me.id, "TAG_LOG"):
            try:
                pr = await check_logger(c)
            except (PeerFlood, UserRestricted, UserBannedInChannel):
                return await xx.edit(_("lim_er").format(em.gagal))
            babi = await c.export_chat_invite_link(int(pr))
            dB.set_var(c.me.id, "TAG_LOG", int(pr))
            return await xx.edit(_("grplog_1").format(em.sukses, babi))
        else:
            return await xx.edit(_("grplog_2").format(em.sukses))
    if cek.lower() == "off":
        if dB.get_var(c.me.id, "TAG_LOG"):
            xx = dB.get_var(c.me.id, "TAG_LOG")
            try:
                await c.delete_supergroup(int(xx))
                dB.remove_var(c.me.id, "TAG_LOG")
                return await xx.edit(_("grplog_3").format(em.gagal))
            except Exception as e:
                return f"{e}"
        else:
            return await xx.edit(_("grplog_4").format(em.gagal))
    else:
        return await xx.edit(_("grplog_5").format(em.gagal))


@ky.nocmd("LOGS_GROUP", nlx)
@capture_err
# @manage_handlers
async def _(client, message, _):
    log = dB.get_var(client.me.id, "TAG_LOG")
    if not log:
        return
    if message.chat.id == 777000:
        return
    from_user = (
        message.chat if message.chat.type == ChatType.PRIVATE else message.from_user
    )
    if message.sender_chat:
        if message.sender_chat.username is None:
            user_link = f"{message.sender_chat.title}"
        else:
            user_link = f"[{message.sender_chat.title}](https://t.me/{message.sender_chat.username}"
    else:
        user_link = f"[{message.from_user.first_name} {message.from_user.last_name or ''}](tg://user?id={message.from_user.id})"
    message_link = (
        message.link
        if message.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP)
        else f"tg://openmessage?user_id={from_user.id}&message_id={message.id}"
    )
    if message.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:
        text = f"""
📨 <b><u>Group Notifications</u></b>

• <b>Name Group: {message.chat.title}</b>
• <b>ID Group:</b> <code>{message.chat.id}</code>
• <b>From: {user_link}</b>
• <b>Message:</b> <blockquote>{message.text}</blockquote>
• <b>Link Message: [Here]({message_link}) </blockquote>
"""
        try:
            await asyncio.sleep(0.5)
            return await client.send_message(
                int(log), text, disable_web_page_preview=True
            )
        except ChatForwardsRestricted:
            return f"Error ChatForwardsRestricted {message.chat.id}"
        except MessageIdInvalid:
            return f"Error MessageIdInvalid {message.chat.id}"
        except ChannelPrivate:
            return f"Error ChannelPrivate {message.chat.id}"
        except FloodWait as e:
            await asyncio.sleep(e.value)
            return await client.send_message(
                int(log), text, disable_web_page_preview=True
            )
    else:
        text = f"""
📨 <b><u>Private Notifications</u></b>

• <b>From: {user_link}</b>
• <b>Message:</b> <blockquote>{message.text}</blockquote>
• <b>Link Message: [Here]({message_link}) </b>
"""
        try:
            await asyncio.sleep(0.5)
            await client.send_message(
                int(log), text, disable_web_page_preview=True
            )
            return await message.forward(int(log))
        except ChatForwardsRestricted:
            pass
        except MessageIdInvalid:
            pass
        except ChannelPrivate:
            pass
        except FloodWait as e:
            await asyncio.sleep(e.value)
            await client.send_message(
                int(log), text, disable_web_page_preview=True
            )
            return await message.forward(int(log))
