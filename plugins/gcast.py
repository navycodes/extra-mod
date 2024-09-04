################################################################
"""
 Mighty-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


import asyncio

from pyrogram.errors import *
from Userbot import *

from .gcspam import extract_type_and_msg

__MODULES__ = "Broadcast"


def help_string(org):
    return h_s(org, "help_gcast")


@ky.ubot("bc")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    msg = await m.reply(f"{em.proses} **Processing...**")
    command, text = extract_type_and_msg(m)
    if command not in ["grup", "user", "all"] or not text:
        await msg.edit(
            "{} **Silahkan gunakan format [`grup`, `user` or `all`] [text/reply text]**".format(
                em.gagal
            )
        )
        return
    blacklist = dB.mmg(c.me.id)
    chats = await c.get_chats_dialog(command)
    done = 0
    failed = 0
    for chat in chats:
        if chat in blacklist or chat in NO_GCAST or chat in DEVS:
            continue
        try:
            await (
                text.copy(chat) if m.reply_to_message else c.send_message(chat, text)
            )
            done += 1
        except (PeerFlood, UserRestricted, UserBannedInChannel):
            return await msg.edit(_("lim_er").format(em.gagal))
        except SlowmodeWait:
            continue
        except ChatWriteForbidden:
            continue
        except Forbidden:
            continue
        except ChatSendPlainForbidden:
            continue
        except FloodWait as e:
            await asyncio.sleep(e.value)
            try:
                await (
                    text.copy(chat)
                    if m.reply_to_message
                    else c.send_message(chat, text)
                )
                done += 1
            except SlowmodeWait:
                pass
        except Exception:
            failed += 1
    await m.reply(
        f"**{em.alive} Broadcast Message**\n{em.sukses} **Success to : `{done}`**\n{em.gagal} **Failed to : `{failed}`**"
    )
    await msg.delete()
    return


@ky.ubot("gcast")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    msg = await m.reply(_("proses").format(em.proses))
    text = c.get_m(m)
    if not text:
        await msg.edit(_("gcs_1").format(em.gagal))
        return
    blacklist = dB.mmg(c.me.id)
    chats = await c.get_chats_dialog("grup")
    done = 0
    failed = 0
    for chat in chats:
        if chat in blacklist or chat in NO_GCAST:
            continue
        try:
            await (
                text.copy(chat) if m.reply_to_message else c.send_message(chat, text)
            )
            done += 1
        except (PeerFlood, UserRestricted, UserBannedInChannel):
            return await msg.edit(_("lim_er").format(em.gagal))
        except SlowmodeWait:
            continue
        except ChatWriteForbidden:
            continue
        except Forbidden:
            continue
        except ChatSendPlainForbidden:
            continue
        except FloodWait as e:
            await asyncio.sleep(e.value)
            try:
                await (
                    text.copy(chat)
                    if m.reply_to_message
                    else c.send_message(chat, text)
                )
                done += 1
            except SlowmodeWait:
                pass
        except Exception:
            failed += 1
    await m.reply(_("gcs_15").format(em.alive, em.sukses, done, em.gagal, failed))
    await msg.delete()
    return


@ky.ubot("ucast")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    msg = await m.reply(_("proses").format(em.proses))
    text = c.get_m(m)
    if not text:
        await msg.edit(_("gcs_1").format(em.gagal))
        return
    blacklist = dB.mmg(c.me.id)
    chats = await c.get_chats_dialog("user")
    done = 0
    failed = 0
    for chat in chats:
        if chat in blacklist or chat in DEVS:
            continue
        try:
            await (
                text.copy(chat) if m.reply_to_message else c.send_message(chat, text)
            )
            done += 1
        except (PeerFlood, UserRestricted, UserBannedInChannel):
            return await msg.edit(_("lim_er").format(em.gagal))
        except SlowmodeWait:
            continue
        except ChatWriteForbidden:
            continue
        except Forbidden:
            continue
        except FloodWait as e:
            await asyncio.sleep(e.value)
            try:
                await (
                    text.copy(chat)
                    if m.reply_to_message
                    else c.send_message(chat, text)
                )
                done += 1
            except SlowmodeWait:
                pass
        except Exception:
            failed += 1
    await m.reply(_("gcs_16").format(em.alive, em.sukses, done, em.gagal, failed))
    await msg.delete()
    return


@ky.ubot("addbl")
@ky.devs("Etbeel")
@ky.deve("addbl")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    pp = await m.reply(_("proses").format(em.proses))
    chat_id = m.chat.id
    blacklist = dB.mmg(c.me.id)
    if chat_id in blacklist:
        return await pp.edit(_("gcs_4").format(em.sukses))
    add_blacklist = dB.add_chat(c.me.id, chat_id)
    if add_blacklist:
        await pp.edit(_("gcs_5").format(em.sukses, m.chat.id, m.chat.title))
        return
    else:
        await pp.edit(_("gcs_6").format(em.sukses, m.chat.id))
        return


@ky.ubot("delbl")
@ky.deve("delbl")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    pp = await m.reply(_("proses").format(em.proses))
    try:
        if not c.get_arg(m):
            chat_id = m.chat.id
        else:
            chat_id = int(m.command[1])
        blacklist = dB.mmg(c.me.id)
        if chat_id not in blacklist:
            return await pp.edit(_("gcs_7").format(em.gagal, m.chat.id, m.chat.title))
        del_blacklist = dB.remove_chat(c.me.id, chat_id)
        if del_blacklist:
            await pp.edit(_("gcs_8").format(em.sukses, chat_id))
            return
        else:
            await pp.edit(_("gcs_9").format(em.gagal, chat_id))
            return
    except Exception as error:
        await pp.edit(str(error))


@ky.ubot("listbl")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    pp = await m.reply(_("proses").format(em.proses))

    msg = _("gcs_10").format(em.sukses, int(len(dB.mmg(c.me.id))))
    for x in dB.mmg(c.me.id):
        try:
            get = await c.get_chat(x)
            msg += _("gcs_11").format(get.title, get.id)
        except:
            msg += _("gcs_12").format(x)
    await pp.delete()
    await m.reply(msg)
    return


@ky.ubot("rmall")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    msg = await m.reply(_("proses").format(em.proses))
    get_bls = dB.mmg(c.me.id)
    if len(get_bls) == 0:
        return await msg.edit(_("gcs_13").format(em.gagal))
    for x in get_bls:
        dB.remove_chat(c.me.id, x)
    return await msg.edit(_("gcs_14").format(em.sukses))


@ky.ubot("send")
async def _(c: nlx, m, _):
    await c.get_users(bot_username)
    if m.reply_to_message:
        chat_id = m.chat.id if len(m.command) < 2 else m.text.split()[1]
        try:
            if m.reply_to_message.reply_markup:
                x = await c.get_inline_bot_results(bot_username, f"_send_ {id(m)}")
                await c.send_inline_bot_result(chat_id, x.query_id, x.results[0].id)
                await m.delete()
                return
        except Exception as error:
            return await m.reply(error)
        else:
            try:
                await m.reply_to_message.copy(chat_id)
                await m.delete()
                return
            except Exception as t:
                return await m.reply(f"{t}")
    else:
        if len(m.command) < 3:
            return
        chat_id, chat_text = m.text.split(None, 2)[1:]
        try:
            if "/" in chat_id:
                to_chat, msg_id = chat_id.split("/")
                await c.send_message(
                    to_chat, chat_text, reply_to_message_id=int(msg_id)
                )
                await m.delete()
                return
            else:
                await c.send_message(chat_id, chat_text)
                await m.delete()
                return
        except Exception as t:
            return await m.reply(f"{t}")
