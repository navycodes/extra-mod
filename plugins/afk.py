from Userbot import *

__MODULES__ = "Afk"


def help_string(org):
    return h_s(org, "help_afk")


@ky.ubot("afk")
async def _(client: nlx, message, _):
    reason = client.get_arg(message)
    afk_handler = AFK_(client, message, reason)
    await afk_handler.set_afk()


@ky.nocmd("AFK", nlx)
@capture_err
async def _(client, message, _):
    afk_handler = AFK_(client, message)
    await afk_handler.get_afk()


@ky.ubot("unafk")
async def _(client, message, _):
    afk_handler = AFK_(client, message)
    await afk_handler.unset_afk()


@ky.ubot("afkdel")
async def _(c: nlx, m, _):
    em = Emojik(c)
    em.initialize()
    if len(m.command) == 1:
        return await m.reply_text(f"{em.gagal} Gunakan format : `afkdel` on/off.")
    chat_id = c.me.id
    state = m.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "on":
        udB.cleanmode_on(chat_id)
        await m.reply_text(f"{em.sukses} Afk Delete Diaktifkan!")
    elif state == "off":
        udB.cleanmode_off(chat_id)
        await m.reply_text(f"{em.gagal} Afk Delete Dinonaktifkan!")
    else:
        await m.reply_text(f"{em.gagal} Gunakan format : `afkdel` on/off.")
