################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


import asyncio
from io import BytesIO

from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.types import *
from Userbot import *

__MODULES__ = "Global"


def help_string(org):
    return h_s(org, "help_global")


@ky.ubot("gban")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    nyet, nt = await c.extract_user_and_reason(m)
    xx = await m.reply(_("proses").format(em.proses))
    if len(m.text.split()) == 1:
        await xx.edit(_("glbl_2").format(em.gagal))
        return
    if nyet in DEVS:
        await xx.edit(_("glbl_3").format(em.gagal))
        return
    alasan = nt if nt else "Anak Dajjal 🗿"
    bs = 0
    gg = 0
    chats = await c.get_chats_dialog("gban")
    try:
        mention = (await c.get_users(nyet)).mention
    except IndexError:
        mention = m.reply_to_message.sender_chat.title if m.reply_to_message else "Anon"
    except PeerIdInvalid:
        return await m.reply_text(_("peer").format(em.gagal))
    except KeyError:
        return await m.reply_text(_("peer").format(em.gagal))
    db_gban = dB.get_list_from_var(c.me.id, "GBANNED")
    for chat in chats:
        if nyet in db_gban:
            await xx.edit(_("glbl_5").format(em.gagal))
            return
        try:
            await c.ban_chat_member(chat, nyet)
            bs += 1
            await asyncio.sleep(0.1)
        except Exception:
            gg += 1
        except FloodWait as e:
            await asyncio.sleep(int(e.value))
            await c.ban_chat_member(chat, nyet)
            bs += 1
            await asyncio.sleep(0.1)

    dB.add_to_var(c.me.id, "GBANNED", nyet)
    await c.block_user(nyet)
    await c.invoke(
        DeleteHistory(peer=(await c.resolve_peer(nyet)), max_id=0, revoke=True)
    )
    mmg = _("glbl_6").format(
        em.warn, em.sukses, bs, em.gagal, gg, em.profil, mention, em.block, alasan
    )
    await xx.delete()
    return await m.reply(mmg)


@ky.ubot("ungban")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    nyet, nt = await c.extract_user_and_reason(m)
    xx = await m.reply(_("proses").format(em.proses))
    if len(m.text.split()) == 1:
        await xx.edit(_("glbl_2").format(em.gagal))
        return
    bs = 0
    gg = 0
    chats = await c.get_chats_dialog("gban")
    try:
        mention = (await c.get_users(nyet)).mention
    except IndexError:
        mention = m.reply_to_message.sender_chat.title if m.reply_to_message else "Anon"
    except PeerIdInvalid:
        return await m.reply_text(_("peer").format(em.gagal))
    except KeyError:
        return await m.reply_text(_("peer").format(em.gagal))
    db_gban = dB.get_list_from_var(c.me.id, "GBANNED")
    for chat in chats:
        if nyet not in db_gban:
            await xx.edit(_("glbl_7").format(em.gagal))
            return
        try:
            await c.unban_chat_member(chat, nyet)
            bs += 1
            await asyncio.sleep(0.1)
        except Exception:
            gg += 1
            await asyncio.sleep(0.1)
    dB.remove_from_var(c.me.id, "GBANNED", nyet)
    await c.unblock_user(nyet)
    mmg = _("glbl_8").format(em.warn, em.sukses, bs, em.gagal, gg, em.profil, mention)
    await xx.delete()
    return await m.reply(mmg)


@ky.ubot("gmute")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    nyet, nt = await c.extract_user_and_reason(m)
    xx = await m.reply(_("proses").format(em.proses))
    if len(m.text.split()) == 1:
        await xx.edit(_("glbl_2").format(em.gagal))
        return
    if nyet in DEVS:
        await xx.edit(_("glbl_3").format(em.gagal))
        return
    alasan = nt if nt else "Anak Dajjal 🗿"
    bs = 0
    gg = 0
    chats = await c.get_chats_dialog("grup")
    try:
        mention = (await c.get_users(nyet)).mention
    except IndexError:
        mention = m.reply_to_message.sender_chat.title if m.reply_to_message else "Anon"
    except PeerIdInvalid:
        return await m.reply_text(_("peer").format(em.gagal))
    except KeyError:
        return await m.reply_text(_("peer").format(em.gagal))
    db_gmute = dB.get_list_from_var(c.me.id, "GMUTE")
    for chat in chats:
        if nyet in db_gmute:
            await xx.edit(_("glbl_10").format(em.gagal))
            return
        try:
            await c.restrict_chat_member(chat, nyet, ChatPermissions())
            bs += 1
            await asyncio.sleep(0.1)
        except Exception:
            gg += 1
            await asyncio.sleep(0.1)
    dB.add_to_var(c.me.id, "GMUTE", nyet)
    mmg = _("glbl_11").format(
        em.warn, em.sukses, bs, em.gagal, gg, em.profil, mention, em.block, alasan
    )
    await xx.delete()
    return await m.reply(mmg)


@ky.ubot("ungmute")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    nyet, nt = await c.extract_user_and_reason(m)
    xx = await m.reply(_("proses").format(em.proses))
    await c.get_users(nyet)
    if len(m.text.split()) == 1:
        await xx.edit(_("glbl_2").format(em.gagal))
        return
    bs = 0
    gg = 0
    chats = await c.get_chats_dialog("grup")
    try:
        mention = (await c.get_users(nyet)).mention
    except IndexError:
        mention = m.reply_to_message.sender_chat.title if m.reply_to_message else "Anon"
    except PeerIdInvalid:
        return await m.reply_text(_("peer").format(em.gagal))
    except KeyError:
        return await m.reply_text(_("peer").format(em.gagal))
    db_gmute = dB.get_list_from_var(c.me.id, "GMUTE")
    for chat in chats:
        if nyet not in db_gmute:
            await xx.edit(_("glbl_12").format(em.gagal))
            return
        try:
            await c.unban_member(chat, nyet, ChatPermissions())
            bs += 1
            await asyncio.sleep(0.1)
        except Exception:
            gg += 1
            await asyncio.sleep(0.1)
    dB.remove_from_var(c.me.id, "GMUTE", nyet)
    mmg = _("glbl_13").format(em.warn, em.sukses, bs, em.gagal, gg, em.profil, mention)
    await xx.delete()
    return await m.reply(mmg)


@ky.ubot("gbanlist|listgban")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    db_gban = dB.get_list_from_var(c.me.id, "GBANNED")
    msg = await m.reply(_("proses").format(em.proses))

    if db_gban is None:
        return await msg.edit(_("glbl_22").format(em.gagal))
    dftr = _("glbl_14").format(em.profil)
    for ii in db_gban:
        dftr += _("glbl_15").format(em.block, ii)
    try:
        await m.reply_text(dftr)
    except MessageTooLong:
        with BytesIO(str.encode(await remove_markdown_and_html(dftr))) as f:
            f.name = "gbanlist.txt"
            await m.reply_document(document=f, caption=_("glbl_17").format(em.profil))
    return await msg.delete()


@ky.ubot("gmutelist|listgmute")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    gmnu = dB.get_list_from_var(c.me.id, "GMUTE")
    msg = await m.reply(_("proses").format(em.proses))
    if gmnu is None:
        await msg.edit(_("glbl_2").format(em.gagal))
        return
    dftr = _("glbl_18").format(em.profil)
    for ii in gmnu:
        dftr += _("glbl_19").format(em.warn, ii)
    try:
        await m.reply_text(dftr)
    except MessageTooLong:
        with BytesIO(str.encode(await remove_markdown_and_html(dftr))) as f:
            f.name = "gmutelist.txt"
            await m.reply_document(document=f, caption=_("glbl_21").format(em.profil))
    return await msg.delete()


@ky.ubot("addgagu")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    nyet, nt = await c.extract_user_and_reason(m)
    xx = await m.reply(_("proses").format(em.proses))
    if not nyet:
        await xx.edit(_("glbl_2").format(em.gagal))
        return
    # if nyet in DEVS:
    # await xx.edit(_("glbl_3").format(em.gagal))
    # return
    try:
        mention = (await c.get_users(nyet)).mention
    except IndexError:
        mention = m.reply_to_message.sender_chat.title if m.reply_to_message else "Anon"
    except PeerIdInvalid:
        return await m.reply_text(_("peer").format(em.gagal))
    except KeyError:
        return await m.reply_text(_("peer").format(em.gagal))
    db_gmute = dB.get_list_from_var(c.me.id, "ANTI_USER", "USERS")
    if nyet in db_gmute:
        return await xx.edit(_("glbl_10").format(em.gagal))
    try:
        dB.add_to_var(c.me.id, "ANTI_USER", nyet, "USERS")
        mmg = "{} <b> Pengguna {}\n{} Berhasil ditambahkan ke database Gagu</b>".format(
            em.warn, mention, em.sukses
        )
        await xx.delete()
        return await m.reply(mmg)
    except Exception as e:
        await xx.delete()
        return await m.reply(_("err").format(em.gagal, str(e)))


@ky.ubot("delgagu")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    nyet, nt = await c.extract_user_and_reason(m)
    xx = await m.reply(_("proses").format(em.proses))
    if not nyet:
        await xx.edit(_("glbl_2").format(em.gagal))
        return
    try:
        mention = (await c.get_users(nyet)).mention
    except IndexError:
        mention = m.reply_to_message.sender_chat.title if m.reply_to_message else "Anon"
    except PeerIdInvalid:
        return await m.reply_text(_("peer").format(em.gagal))
    except KeyError:
        return await m.reply_text(_("peer").format(em.gagal))
    db_gmute = dB.get_list_from_var(c.me.id, "ANTI_USER", "USERS")

    if nyet not in db_gmute:
        await xx.edit(_("glbl_12").format(em.gagal))
        return
    try:
        dB.remove_from_var(c.me.id, "ANTI_USER", nyet, "USERS")
        mmg = "{} <b> Pengguna {}\n{} Berhasil dihapus dari database Gagu</b>".format(
            em.warn, mention, em.sukses
        )
        await xx.delete()
        return await m.reply(mmg)
    except Exception:
        await xx.delete()
        return await m.reply(_("err").format(em.gagal, str(e)))


@ky.ubot("listgagu")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    gmnu = dB.get_list_from_var(c.me.id, "ANTI_USER", "USERS")
    msg = await m.reply(_("proses").format(em.proses))
    if gmnu is None:
        await msg.edit(_("glbl_2").format(em.gagal))
        return
    dftr = "{} <b>Daftar Pengguna Gagu:\n</b>".format(em.profil)
    for ii in gmnu:
        dftr += "{} Makhluk -> {}".format(em.warn, ii)
    try:
        await m.reply_text(f"<b>{dftr}</b>")
    except MessageTooLong:
        with BytesIO(str.encode(await remove_markdown_and_html(dftr))) as f:
            f.name = "gagulist.txt"
            await m.reply_document(document=f, caption=_("glbl_21").format(em.profil))
    return await msg.delete()


@ky.nocmd("ANTIUSER", nlx)
@capture_err
async def _(c, m, _):
    lisu = dB.get_list_from_var(c.me.id, "ANTI_USER", "USERS")
    user = m.from_user.id if m.from_user.id else None
    if user in lisu:
        try:
            await c.delete_messages(m.chat.id, user)
            return
        except Exception as e:
            return await m.reply(f"Error Gagu {str(e)}")
