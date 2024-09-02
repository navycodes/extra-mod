from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.methods import *
from pyrogram.types import *
from Userbot import *

__MODULES__ = "Invite"


def help_string(org):
    return h_s(org, "help_invite")


@ky.ubot("invite|undang")
@ky.devs("sinijoin")
async def _(c, m, _):
    em = Emojik(c)
    em.initialize()
    mg = await m.reply_text(_("inv_1").format(em.proses))
    if len(m.command) < 2:
        await mg.edit(_("inv_2").format(em.gagal))
        return

    user_s_to_add = m.command[1]
    user_list = user_s_to_add.split(" ")
    user_id = await c.extract_user(m)

    if not user_list:
        await mg.edit(_("inv_2").format(em.gagal))
        return
    try:
        await c.add_chat_members(m.chat.id, user_list, forward_limit=100)
    except PeerIdInvalid:
        await mg.edit(_("peer").format(em.gagal))
        return
    except UserAlreadyParticipant:
        await m.delete()
        return await mg.delete()
    except KeyError:
        await mg.edit(_("keyeror").format(em.gagal))
        return
    mention = (await c.get_users(user_id)).mention
    await mg.edit(_("inv_3").format(em.sukses, mention, m.chat.title))
    return


@ky.ubot("getlink|invitelink")
@ky.devs("getling")
async def _(c, m, _):
    em = Emojik(c)
    em.initialize()
    Nan = await m.reply_text(_("proses").format(em.proses))

    if m.chat.type in [ChatType.GROUP, ChatType.SUPERGROUP]:

        try:
            link = await c.export_chat_invite_link(m.chat.id)
            await Nan.edit(_("inv_4").format(em.sukses, link))
            return
        except Exception:
            await Nan.edit(_("inv_5").format(em.gagal))
            return
    elif m.chat.type == ChatType.CHANNEL:
        try:
            link = await c.export_chat_invite_link(m.chat.id)
            await Nan.edit(_("inv_4").format(em.sukses, link))
            return
        except Exception:
            await Nan.edit(_("inv_5").format(em.gagal))
            return
    else:
        return await Nan.edit(_("inv_6").format(em.gagal))
