################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || Gojo_Satoru
"""
################################################################

from datetime import datetime

from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.raw.functions.channels import GetFullChannel
from Userbot import *

gban_db = GBan()

__MODULES__ = "Info"


def help_string(org):
    return h_s(org, "help_info")


async def count(c, chat):
    em = Emojik(c)
    em.initialize()
    try:
        administrator = []
        async for admin in c.get_chat_members(
            chat_id=chat, filter=ChatMembersFilter.ADMINISTRATORS
        ):
            administrator.append(admin)
        total_admin = administrator
        bot = []
        async for tbot in c.get_chat_members(
            chat_id=chat, filter=ChatMembersFilter.BOTS
        ):
            bot.append(tbot)

        total_bot = bot
        bot_admin = 0
        ban = []
        async for banned in c.get_chat_members(chat, filter=ChatMembersFilter.BANNED):
            ban.append(banned)

        total_banned = ban
        for x in total_admin:
            for y in total_bot:
                if x == y:
                    bot_admin += 1
        total_admin = len(total_admin)
        total_bot = len(total_bot)
        total_banned = len(total_banned)
        return total_bot, total_admin, bot_admin, total_banned
    except Exception as e:
        total_bot = total_admin = bot_admin = total_banned = print(f"Error {e}")

    return total_bot, total_admin, bot_admin, total_banned


@ky.ubot("info|whois")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    if m.reply_to_message and m.reply_to_message.sender_chat:
        await m.reply_text(_("info_16").format(em.gagal))
        return
    sus = await c.extract_user(m)
    if not sus:
        await m.reply_text(_("glbl_2").format(em.gagal))
    try:
        user = await c.get_users(sus)
    except KeyError:
        return await m.reply_text(_("keyeror").format(em.gagal))
    except UsernameInvalid:
        return await m.reply_text(_("keyeror").format(em.gagal))
    except PeerIdInvalid:
        return await m.reply_text(_("peer").format(em.gagal))
    full = (
        f"<a href=tg://user?id={user.id}>{user.first_name} {user.last_name or ''}</a>"
    )
    dict_userinfo = {
        "name": full,
        "id": user.id,
        "contact": user.is_contact,
        "premium": user.is_premium,
        "deleted": user.is_deleted,
        "isbot": user.is_bot,
        "dc_id": user.dc_id,
    }
    udB.set_var(c.me.id, "user_info", dict_userinfo)
    try:
        x = await c.get_inline_bot_results(bot_username, "user_info")
        await c.send_inline_bot_result(
            m.chat.id, x.query_id, x.results[0].id, reply_to_message_id=m.id
        )
    except Exception as e:
        return await m.edit(_("err").format(em.gagal, str(e)))


@ky.ubot("cinfo|chatinfo")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    splited = m.text.split()
    if len(splited) == 1:
        if m.reply_to_message and m.reply_to_message.sender_chat:
            chat = m.reply_to_message.sender_chat.id
        else:
            chat = m.chat.id

    else:
        chat = splited[1]

    try:
        chat = int(chat)
    except (ValueError, Exception) as ef:
        if "invalid literal for int() with base 10:" in str(ef):
            chat = str(chat)
            if chat.startswith("https://"):
                chat = "@" + chat.split("/")[-1]
        else:
            return await m.reply_text(_("info_17").format(em.gagal, m.command))
    try:
        gc = await c.get_chat(chat)
    except UsernameInvalid:
        return await m.reply_text(_("keyeror").format(em.gagal))
    except KeyError:
        return await m.reply_text(_("keyeror").format(em.gagal))
    except ChannelInvalid:
        return await m.reply_text(_("keyeror").format(em.gagal))
    except PeerIdInvalid:
        return await m.reply_text(_("peer").format(em.gagal))
    total_bot, total_admin, total_bot_admin, total_banned = await count(c, gc.id)
    i = await c.resolve_peer(gc.id)
    o = await c.invoke(GetFullChannel(channel=i))
    about = o.full_chat.about
    dict_gcinfo = {
        "name": gc.title,
        "id": gc.id,
        "type": str(gc.type).split(".")[1],
        "username": gc.username,
        "member": gc.members_count,
        "protect": gc.has_protected_content,
        "dc_id": gc.dc_id,
        "total_bot": total_bot,
        "total_admin": total_admin,
        "total_bot_admin": total_bot_admin,
        "total_banned": total_banned,
        "desc": about,
    }
    udB.set_var(c.me.id, "gc_info", dict_gcinfo)
    try:
        x = await c.get_inline_bot_results(bot_username, "gc_info")
        await c.send_inline_bot_result(
            m.chat.id, x.query_id, x.results[0].id, reply_to_message_id=m.id
        )
    except Exception as e:
        return await m.edit(_("err").format(em.gagal, str(e)))


@ky.ubot("me|userstats")
@ky.devs("userstats")
async def _(c, m, _):
    em = Emojik(c)
    em.initialize()
    Nan = await m.reply_text(_("proses").format(em.proses))
    start = datetime.now()
    zz = 0
    nanki = 0
    luci = 0
    tgr = 0
    ceger = 0
    kntl = 0
    benet = 0
    dimari = set()
    try:
        async for dialog in c.get_dialogs():
            try:
                if dialog.chat.type == ChatType.PRIVATE:
                    zz += 1
                elif dialog.chat.type == ChatType.BOT:
                    ceger += 1
                elif dialog.chat.type == ChatType.GROUP:
                    nanki += 1
                elif dialog.chat.type == ChatType.SUPERGROUP:
                    luci += 1
                    user_s = await dialog.chat.get_member(c.me.id)
                    if user_s.status in (
                        ChatMemberStatus.OWNER,
                        ChatMemberStatus.ADMINISTRATOR,
                    ):
                        kntl += 1
                elif dialog.chat.type == ChatType.CHANNEL:
                    tgr += 1
            except ChannelPrivate:
                benet += 1
                dimari.add(dialog.chat.id)
                await c.leave_chat(dialog.chat.id)
                print(f"Left chat: {dialog.chat.id}")
                continue
    except ChannelPrivate:
        benet += 1
        dimari.add(dialog.chat.id)

    end = datetime.now()
    ms = (end - start).seconds
    if not dimari:
        dimari = None
    return await Nan.edit_text(
        """
>{} **Succesful extract your data in `{}` seconds
>`{}` Private Messages.
>`{}` Groups.
>`{}` Super Groups.
>`{}` Channels.
>`{}` Admin in Chats.
>`{}` Bots.
>`{}` Group With Trouble
>
>I've trouble with this chat : 
>- `{}`**""".format(
            em.sukses,
            ms,
            zz,
            nanki,
            luci,
            tgr,
            kntl,
            ceger,
            benet,
            dimari,
        )
    )
