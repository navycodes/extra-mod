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
        return await pros.edit(
            "{} Total message from user {} is {} messages".format(
                em.sukses, umention, o
            )
        )
    except Exception as e:
        return await pros.edit(_("err_1").format(em.gagal, str(e)))


@ky.ubot("cekos")
async def _(client, message, _):
    emo = Emojik(client)
    emo.initialize()
    pros = await message.reply(_("proses").format(em.proses))

    chat = message.command[1] if len(message.command) > 1 else message.chat.id
    try:
        if isinstance(chat, int):
            chat_id = chat
        else:
            chat_info = await client.get_chat(chat)
            chat_id = chat_info.id

        try:
            info = await client.get_chat(chat_id)
            title = info.title if info.title else f"{chat_id}"
        except Exception:
            title = f"{chat_id}"
        group_call = await get_group_call(client, message, err_msg="Error")
        if not group_call:
            return await pros.edit(
                "{} <b>Voice chat group not found in {}</b>".format(em.gagal, title)
            )
        try:
            participants = await client.group_call.get_participants(chat_id)
            mentions = []
            for participant in participants:
                user_id = participant.user_id
                try:
                    user = await client.get_users(user_id)
                    mention = user.mention
                    status = "🔈 Silent" if participant.muted else "🔊 Speaking"
                    mentions.append(f"{mention} Status {status}")
                except Exception as e:
                    print(f"{e}")
                    mentions.append(f"{user_id} Status Unknown")

            total_participants = len(participants)
            if total_participants == 0:
                return await pros.edit(
                    "{} <b>No someone in voice chat group!!</b>".format(em.gagal)
                )
            mentions_text = "\n".join(
                [
                    (f"• {mention}" if i < total_participants - 1 else f"• {mention}")
                    for i, mention in enumerate(mentions)
                ]
            )
            text = f"""
{emo.sukses} <b>Voice Chat Listener:</b>
{emo.alive} Chat: <code>{title}</code>.
{emo.profil} Total: <code>{total_participants}</code> Listener.

<b>People:</b>
{mentions_text}
"""
            return await pros.edit(f"<b>{text}</b>")
        except Exception as e:
            return await pros.edit(_("err_1").format(em.gagal, str(e)))
    except Exception as e:
        return await pros.edit(_("err_1").format(em.gagal, str(e)))
