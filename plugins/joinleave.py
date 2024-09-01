import asyncio

from pyrogram.enums import *
from pyrogram.errors import (ChannelPrivate, ChatAdminRequired,
                             UserNotParticipant)
from pyrogram.types import *
from Userbot import *

__MODULES__ = "Join"


def help_string(org):
    return h_s(org, "help_join")


@ky.ubot("join")
@ky.devs("Cjoin")
async def _(c, m, _):
    em = Emojik(c)
    em.initialize()
    Nan = m.command[1] if len(m.command) > 1 else m.chat.id
    ceger = await m.reply_text(_("proses").format(em.proses))
    try:
        chat_id = m.command[1] if len(m.command) > 1 else m.chat.id
        if chat_id.startswith("https://t.me/"):
            chat_id = chat_id.split("/")[-1]
        inpogc = await c.get_chat(Nan)
        namagece = inpogc.title

        await ceger.edit(_("join_1").format(em.sukses, namagece))
        await c.join_chat(Nan)
        return
    except Exception as ex:
        await ceger.edit(_("err").format(em.gagal, ex))
        return


@ky.ubot("kickme")
@ky.devs("Ckickme")
async def _(c, m, _):
    em = Emojik(c)
    em.initialize()
    namagece = m.chat.title
    ceger = await m.reply(_("proses").format(em.proses))
    try:
        chat_member = await c.get_chat_member(m.chat.id, m.from_user.id)
        if chat_member.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER,
        ):
            await ceger.edit(_("join_7").format(em.gagal, namagece))
            return

        if len(m.command) < 2:
            chat_id = m.chat.id
            namagece = m.chat.title
            if chat_id in NO_GCAST:
                await ceger.edit(_("join_2").format(em.gagal, namagece))
                return
            else:
                await ceger.edit(_("join_3").format(em.sukses, c.me.mention, namagece))
                await c.leave_chat(chat_id)
                return

        chat_arg = m.command[1]

        if chat_arg.startswith("@"):
            inpogc = await c.get_chat(chat_arg)
            chat_id = inpogc.id
            namagece = inpogc.title

            if chat_id in NO_GCAST:
                return await ceger.edit(_("join_2").format(em.gagal, namagece))
            else:
                await ceger.edit(_("join_3").format(em.sukses, c.me.mention, namagece))
                await c.leave_chat(chat_id)

        elif chat_arg.startswith("https://t.me/"):
            chat_id = chat_arg.split("/")[-1]
            inpogc = await c.get_chat(chat_id)
            namagece = inpogc.title
            if str(chat_id) in NO_GCAST or inpogc.id in NO_GCAST:
                await ceger.edit(_("join_2").format(em.gagal, namagece))
                return
            else:
                await ceger.edit(_("join_3").format(em.sukses, c.me.mention, namagece))
                await c.leave_chat(chat_id)
                return

        else:
            await m.reply(_("join_4").format(em.sukses))
            await c.leave_chat(chat_id)
            return

    except ChatAdminRequired:
        await m.reply(
            f"{em.gagal} <b>Saya tidak memiliki izin untuk meninggalkan obrolan ini!</b>"
        )
        return
    except UserNotParticipant:
        await m.reply(
            f"{em.gagal} <b>Anda bukan lagi anggota atau member di <code>{namagece}</code></b>"
        )
        return
    except ChannelPrivate:
        await m.reply(
            f"{em.gagal} <b>Anda bukan lagi anggota atau member di <code>{namagece}</code></b>"
        )
        return
    except Exception as e:
        await ceger.edit(_("err").format(em.gagal, e))
        return


@ky.ubot("leave")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    xenn = await m.reply(_("proses").format(em.proses))
    ceger = [
        -1001713457115,
        -1001818398503,
        -1001697717236,
        -1001986858575,
        -1001876092598,
        -1001812143750,
        -1002058863067,
    ]
    command = m.text.split(None, 1)[1]
    if command not in ["grup", "ch"]:
        await xenn.edit(f"{em.gagal} **Please give query [`grup` or `ch`]** ")
        return
    luci = 0
    nan = 0
    chats = await c.get_chats_dialog(command)
    for chat in chats:
        if chat in ceger:
            continue
        try:
            chat_info = await c.get_chat_member(chat, "me")
            user_status = chat_info.status
            if user_status not in (
                ChatMemberStatus.OWNER,
                ChatMemberStatus.ADMINISTRATOR,
            ):
                luci += 1
                await c.leave_chat(chat)
        except FloodWait as e:
            await asyncio.sleep(e)
            await c.leave_chat(chat)
            luci += 1
        except Exception:
            nan += 1
        except Exception as e:
            print(f"An error occurred while fetching dialogs: {e}")
    await xenn.delete()
    await m.reply(
        f"{em.sukses} **Success to leave : `{luci}`\n{em.gagal} Failed to leave : `{nan}`**"
    )
    return


@ky.ubot("leavemute")
async def _(c, m, _):
    em = Emojik(c)
    em.initialize()
    xenn = await m.reply_text(_("proses").format(em.proses))
    luci = 0
    nan = 0
    ceger = [-1002058863067, -1001986858575, -1001876092598, -1001812143750]
    chats = await c.get_chats_dialog("grup")
    for chat in chats:
        if chat in ceger:
            continue
        try:
            try:
                chat_info = await c.get_chat_member(chat, "me")
                user_status = chat_info.status
                if user_status == ChatMemberStatus.RESTRICTED:
                    nan += 1
                    await c.leave_chat(chat)
            except FloodWait as e:
                await asyncio.sleep(e)
                await c.leave_chat(chat)
                nan += 1
            except Exception:
                luci += 1
        except Exception as e:
            print(f"An error occurred while fetching dialogs: {e}")

    await xenn.delete()
    await m.reply(
        f"{em.sukses} **Success to leave : `{nan}`\n{em.gagal} Failed to leave : `{luci}`**"
    )
    return
